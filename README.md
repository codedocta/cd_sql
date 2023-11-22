SQLAlchemy Wrapper

This Python package provides a simple and intuitive wrapper for SQLAlchemy, making it easier to work with SQL databases in Python. It abstracts the complexities of direct SQLAlchemy usage, offering a streamlined API for database operations.

Features

Easy to use interface for database connections and operations.
Supports executing custom SQL queries.
Methods for fetching single or multiple records.
Error handling for database operations.

Installation

To install the package, use pip:

pip install cd-sql

To get updates:

pip install --upgrade cd-sql

Usage

Connecting to a Database

from cd_sql import SQL

# Create an instance with the connection string
db = SQL('sqlite:///example.db')

# Connect to the database
db.connect()


Executing Queries

# Execute a custom query
result = db.execute_query('SELECT * FROM my_table')

# Fetch all records
records = db.fetch_all('SELECT * FROM my_table')

# Fetch a single record
record = db.fetch_one('SELECT * FROM my_table WHERE id = 1')


Disconnecting

# Disconnect from the database when done
db.disconnect()


# Queries
### note: This is to be used in the SQL class and are helper methods to aid in your DB queries.
This Python library provides a set of common SQL query utilities, making it easier to interact with databases using structured queries. It's designed to work with any database class that follows a specific interface for executing SQL commands.

# Features

Simplified methods for common SQL operations.
Supports SELECT, INSERT, UPDATE, DELETE, and custom queries.
Methods for table creation, deletion, and truncation.
Counting rows in a table.


Usage

Basic Operations

from cd_sql import CommonQueries

db_instance = YourDatabaseClass()
queries = CommonQueries(db_instance)

# Select all records from a table
records = queries.select_all('my_table')

# Insert a record into a table
queries.insert('my_table', ['column1', 'column2'], ['value1', 'value2'])

# Update a record in a table
queries.update('my_table', ['column1'], ['new_value'], 'id', 1)

# Delete a record from a table
queries.delete('my_table', 'id', 1)


Advanced Operations

# Count rows in a table
row_count = queries.count_rows('my_table')

# Create a new table
queries.create_table('new_table', ['id INTEGER PRIMARY KEY', 'name TEXT'])

# Delete a table
queries.delete_table('old_table')

# Execute a custom query
result = queries.custom_query('SELECT * FROM my_table WHERE column1 = ?', ['value1'])

## More documentation at:
[Code Docta](https://codedocta.com "Code Docta")


## Contributing

Contributions to the package are welcome. Please follow the standard GitHub pull request process to propose changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
