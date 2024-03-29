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

## Connecting examples

### SQLite

SQLite is a lightweight, file-based database. It doesn't require a separate server process.

```python
from sql_class import SQL

# SQLite connection string format: 'sqlite:///path_to_database_file.db'
db = SQL('sqlite:///my_database.db')
db.connect()
```

### MySQL

MySQL is a popular open-source relational database management system.

```python
from sql_class import SQL

# MySQL connection string format: 'mysql+pymysql://user:password@host:port/database'
db = SQL('mysql+pymysql://username:password@localhost/my_database')
db.connect()
```

### PostgreSQL

PostgreSQL is an advanced open-source relational database.

```python
from sql_class import SQL

# PostgreSQL connection string format: 'postgresql://user:password@host:port/database'
db = SQL('postgresql://username:password@localhost/my_database')
db.connect()
```

### Microsoft SQL Server

Microsoft SQL Server is a relational database management system developed by Microsoft.

```python
from sql_class import SQL

# MS SQL Server connection string format: 'mssql+pyodbc://user:password@host:port/database'
db = SQL('mssql+pyodbc://username:password@localhost/my_database')
db.connect()
```

### Oracle

Oracle Database is a multi-model database management system produced and marketed by Oracle Corporation.

```python
from sql_class import SQL

# Oracle connection string format: 'oracle+cx_oracle://user:password@host:port/?sid=database'
db = SQL('oracle+cx_oracle://username:password@localhost:1521/?sid=my_database')
db.connect()
```

### Notes:

- Replace `username`, `password`, `localhost`, `port`, and `my_database` with your actual database credentials and details.
- For MySQL, PostgreSQL, Microsoft SQL Server, and Oracle, you might need to install additional drivers or Python packages (like `pymysql`, `psycopg2`, `pyodbc`, `cx_oracle`) to establish the connection.
- The connection strings are formatted according to SQLAlchemy's URL format. Ensure that the format matches the version of SQLAlchemy you are using.

The core API of the `SQL` class you've designed will not need to change to accommodate different databases like MySQL, PostgreSQL, Microsoft SQL Server, or Oracle. The flexibility of SQLAlchemy, which your class is based on, allows it to work with various databases without altering the primary interface for executing queries, connecting, or disconnecting.

However, there are a few considerations to keep in mind:

1. **Database Drivers and Dependencies**: While the API remains the same, the underlying database drivers required to connect to different databases vary. For instance, connecting to MySQL might require `pymysql` or `mysql-connector-python`, PostgreSQL might need `psycopg2`, SQL Server might require `pyodbc`, and Oracle might need `cx_Oracle`. These drivers should be installed separately as they are not included with SQLAlchemy.

2. **Connection Strings**: The format of the connection string varies depending on the database. Users of your `SQL` class will need to provide the correct connection string format for the specific database they are connecting to. This is a user responsibility and does not require changes to your class.

3. **Database-Specific Features**: Some databases have unique features or SQL syntax variations. While basic SQL operations (like SELECT, INSERT, UPDATE, DELETE) are generally consistent across databases, more advanced features or optimizations might differ. If your class or application needs to leverage these advanced features, additional methods or conditional logic might be required.

4. **Error Handling**: Different databases might throw different exceptions for similar error conditions. While SQLAlchemy does a good job of abstracting many of these, there might be cases where database-specific error handling is necessary.

5. **Documentation and Examples**: It would be beneficial to provide documentation or examples showing how to use your class with different databases, including the installation of necessary drivers and the correct format for connection strings.

