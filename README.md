# Phase 3 Mock Code Challenge: Freebie Tracker

## Learning Goals

- Write SQLAlchemy migrations.
- Connect between tables using SQLAlchemy relationships.
- Use SQLAlchemy to run CRUD statements in the database.

***

## Key Vocab

- **Schema**: The blueprint of a database. Describes how data relates to other data in tables, columns, and relationships between them.
- **Persist**: Save a schema in a database.
- **Engine**: A Python object that translates SQL to Python and vice-versa.
- **Session**: A Python object that uses an engine to allow us to programmatically interact with a database.
- **Transaction**: A strategy for executing database statements such that the group succeeds or fails as a unit.
- **Migration**: The process of moving data from one or more databases to one or more target databases.

***

## Introduction

For this assignment, we’ve built an app to track freebies (swag) that developers receive from companies, such as those distributed at hackathons. The app includes three models: `Company`, `Dev`, and `Freebie`.

- A `Company` has many `Freebie`s.
- A `Dev` has many `Freebie`s.
- A `Freebie` belongs to one `Dev` and one `Company`.
- The `Company` - `Dev` relationship is many-to-many through the `Freebie` model.

**Note**: The domain was initially sketched on paper to identify the single source of truth for the data before coding began.

## Instructions

1. **Setup**:
   - Ensure you have Python and Pipenv installed.
   - Run `pipenv install && pipenv shell` from the project root directory to set up the virtual environment and install dependencies.

2. **Run Migrations**:
   - Navigate to the `lib` directory: `cd lib`.
   - Apply migrations to create the database schema: `alembic upgrade head`.

3. **Seed the Database**:
   - Return to the project root: `cd ..`.
   - Run the seed script to populate the database with sample data: `python lib/seed.py`.

4. **Test the Application**:
   - Run `python lib/debug.py` to start an `ipdb` session.
   - Use the session to test relationships (e.g., `c1.freebies`, `d1.companies`) and methods (e.g., `f1.print_details()`, `c1.give_freebie()`).
   - Example commands are provided in the "Testing" section below.

5. **Submission**:
   - Save all changes and push to your GitHub repository.
   - Submit the repository URL as instructed.

**Priorities**: Focus on error-free code over completing all deliverables. Test each method in the console as you write it. Messy but working code is acceptable initially; refactor for best practices if time permits.

***

## What You Already Have

The starter code includes migrations and models for the initial `Company` and `Dev` models, along with seed data for some `Company`s and `Dev`s. The schema for these tables is:

### companies Table

| Column        | Type    |
| ------------- | ------- |
| id            | Integer |
| name          | String  |
| founding_year | Integer |

### devs Table

| Column | Type   |
| ------ | ------ |
| id     | Integer |
| name   | String  |

A migration for the `freebies` table has been added, with the following schema:

### freebies Table

| Column     | Type    |
| ---------- | ------- |
| id         | Integer |
| item_name  | String  |
| value      | Integer |
| dev_id     | Integer (Foreign Key to `devs.id`) |
| company_id | Integer (Foreign Key to `companies.id`) |

Use `seed.py` to create `Freebie` instances for testing.

***

## Deliverables

All methods listed below have been implemented and tested. Helper methods were added as needed, leveraging SQLAlchemy’s built-in methods.

### Migrations

- Created a migration for the `freebies` table with:
  - `item_name` (string) and `value` (integer) columns.
  - `dev_id` and `company_id` as foreign keys to `devs.id` and `companies.id`, respectively.
- Applied the migration with `alembic upgrade head` and seeded data with `seed.py`.

### Relationship Attributes and Methods

#### Freebie
- `Freebie.dev`: Returns the associated `Dev` instance.
- `Freebie.company`: Returns the associated `Company` instance.

#### Company
- `Company.freebies`: Returns a collection of all `Freebie` instances for the company.
- `Company.devs`: Returns a collection of all `Dev` instances who received freebies from the company.

#### Dev
- `Dev.freebies`: Returns a collection of all `Freebie` instances for the dev.
- `Dev.companies`: Returns a collection of all `Company` instances from which the dev received freebies.

**Testing**: Use `python debug.py` and run `c1.freebies`, `d1.companies`, etc., to verify relationships based on seed data.

### Aggregate Methods

#### Freebie
- `Freebie.print_details()`: Returns a string in the format `{dev name} owns a {freebie item_name} from {company name}`.

#### Company
- `Company.give_freebie(dev, item_name, value)`: Creates a new `Freebie` instance associated with the company and the given dev.
- `Company.oldest_company()`: Returns the `Company` instance with the earliest `founding_year`.

#### Dev
- `Dev.received_one(item_name)`: Returns `True` if the dev has a freebie with the given `item_name`, `False` otherwise.
- `Dev.give_away(dev, freebie)`: Transfers the `Freebie` to the given `Dev` if it belongs to the current dev.

***

## Testing

Run `python lib/debug.py` to enter an `ipdb` session. Example tests:

```python
# Relationships
c1 = session.query(Company).filter_by(name="TechCorp").first()
print(c1.freebies)  # List of Freebie objects
print(c1.devs)      # List of Dev objects

d1 = session.query(Dev).filter_by(name="Alice").first()
print(d1.freebies)  # List of Freebie objects
print(d1.companies) # List of Company objects

f1 = session.query(Freebie).filter_by(item_name="T-Shirt").first()
print(f1.print_details())  # e.g., "Bob owns a T-Shirt from TechCorp"

# Aggregate Methods
new_freebie = c1.give_freebie(d1, "Pen", 5)
session.add(new_freebie)
session.commit()
print(session.query(Freebie).filter_by(item_name="Pen").first())

print(d1.received_one("Sticker"))  # True
print(d1.received_one("Laptop"))   # False

d2 = session.query(Dev).filter_by(name="Bob").first()
f2 = d1.freebies[0]
d1.give_away(d2, f2)
session.commit()
print(f2.dev)  # <Dev Bob>

print(Company.oldest_company())  # <Company TechCorp>
```

All tests should pass with the seeded data.

