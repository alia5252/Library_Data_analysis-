import sqlite3
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "data" / "library_analytics.db"


def main():
    connection = sqlite3.connect(DATABASE_PATH)

    transactions = pd.read_sql_query(
        "SELECT * FROM borrow_transactions",
        connection
    )

    books = pd.read_sql_query(
        "SELECT * FROM books",
        connection
    )

    borrowers = pd.read_sql_query(
        "SELECT * FROM borrowers",
        connection
    )

    print()
    print("=== TRANSACTIONS INFO ===")
    print(transactions.info())

    print()
    print("=== MISSING VALUES ===")
    print(transactions.isnull().sum())

    print()
    print("=== NUMERICAL SUMMARY ===")
    print(transactions.describe())
       connection.close()

    print("All datasets loaded successfully.")
    print()
if __name__ == "__main__":
    main()