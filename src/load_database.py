import csv
import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATABASE_PATH = DATA_DIR / "library_analytics.db"


def connect_database():
    return sqlite3.connect(DATABASE_PATH)


def load_books(connection):
    file_path = DATA_DIR / "books.csv"

    with file_path.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        rows = [
            (
                int(row["book_id"]),
                row["title"],
                row["author"],
                row["category"],
                int(row["quantity"]),
            )
            for row in reader
        ]

    connection.executemany(
        """
        INSERT INTO books (
            book_id,
            title,
            author,
            category,
            quantity
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        rows,
    )

    print(f"Loaded {len(rows)} books")


def load_borrowers(connection):
    file_path = DATA_DIR / "borrowers.csv"

    with file_path.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        rows = [
            (
                row["borrower_id"],
                row["borrower_name"],
            )
            for row in reader
        ]

    connection.executemany(
        """
        INSERT INTO borrowers (
            borrower_id,
            borrower_name
        )
        VALUES (?, ?)
        """,
        rows,
    )

    print(f"Loaded {len(rows)} borrowers")


def load_transactions(connection):
    file_path = DATA_DIR / "borrow_transactions.csv"

    with file_path.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        rows = [
            (
                row["borrow_id"],
                int(row["book_id"]),
                row["borrower_id"],
                row["borrow_date"],
                row["due_date"],
                row["return_date"] or None,
                float(row["fine"]),
                1 if row["returned"] == "True" else 0,
            )
            for row in reader
        ]

    connection.executemany(
        """
        INSERT INTO borrow_transactions (
            borrow_id,
            book_id,
            borrower_id,
            borrow_date,
            due_date,
            return_date,
            fine,
            returned
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )

    print(f"Loaded {len(rows)} transactions")


def main():
    connection = connect_database()

    try:
        load_books(connection)
        load_borrowers(connection)
        load_transactions(connection)

        connection.commit()

        print("Database loading completed successfully.")

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


if __name__ == "__main__":
            main()