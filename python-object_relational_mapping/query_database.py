#!/usr/bin/python3
"""
A script to interact with a MySQL database and retrieve records.
This script demonstrates handling cases with varying numbers of results.

Usage: ./query_database.py <host> <username> <password> <database>
"""
import MySQLdb
import sys


def main():
    if len(sys.argv) != 5:
        print("Usage: ./query_database.py <host> <username> <password> <database>")
        return

    host, user, passwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        # Connect to the database
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db_name)
        cursor = db.cursor()

        # Execute a query (Example: Fetch all rows from `my_table`)
        cursor.execute("SELECT * FROM my_table")
        rows = cursor.fetchall()

        # Output the results
        for row in rows:
            print(row)

        # Handle different cases
        if len(rows) == 0:
            print("No records found.")
        elif len(rows) <= 2:
            print(f"Found {len(rows)} record(s): {rows}")
        elif len(rows) >= 100000:
            print(f"Handling large dataset of {len(rows)} records.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        if 'db' in locals() and db:
            db.close()


if __name__ == "__main__":
    main()

