import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
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
    transactions.info()

    print()
    print("=== MISSING VALUES ===")
    print(transactions.isnull().sum())

    print()
    print("=== NUMERICAL SUMMARY ===")
    print(transactions.describe())

    print()
    print("=== RETURN STATUS ANALYSIS ===")

    returned_count = (transactions["return_date"].notna()).sum()
    not_returned_count = transactions["return_date"].isna().sum()

    print("Returned:", returned_count)
    print("Not Returned:", not_returned_count)

    print()
    print("=== FINE ANALYSIS ===")

    total_fine = transactions["fine"].sum()
    average_fine = transactions["fine"].mean()
    maximum_fine = transactions["fine"].max()
    fine_transactions = (transactions["fine"] > 0).sum()

    print("Total Fine:", total_fine)
    print("Average Fine:", average_fine)
    print("Maximum Fine:", maximum_fine)
    print("Transactions With Fine:", fine_transactions)


    print()
    print("=== TOP 10 MOST BORROWED BOOKS ===")

    book_borrow_counts = (
        transactions
        .groupby("book_id")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    print(book_borrow_counts)

    print()
    print("=== TOP 10 MOST ACTIVE BORROWERS ===")

    borrower_counts = (
        transactions
        .groupby("borrower_id")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    print(borrower_counts)

    print()
    print("=== BORROWINGS BY CATEGORY ===")

    # Requires books.category and a join on book_id
    merged = transactions.merge(books[["book_id", "category"]], on="book_id", how="left")

    category_counts = (
        merged
        .groupby("category")
        .size()
        .sort_values(ascending=False)
    )

    print(category_counts)

    print()
    print("=== MONTHLY BORROWING TREND ===")

    transactions["borrow_date"] = pd.to_datetime(transactions["borrow_date"])
    transactions["borrow_month"] = transactions["borrow_date"].dt.to_period("M")

    monthly_trend = (
        transactions
        .groupby("borrow_month")
        .size()
        .sort_index()
    )

    print(monthly_trend)

    print()
    print("=== FINE BY CATEGORY ===")

    fine_by_category = (
        merged
        .groupby("category")["fine"]
        .agg(total_fine="sum", average_fine="mean", fine_count=lambda x: (x > 0).sum())
        .sort_values("total_fine", ascending=False)
    )

    print(fine_by_category)

    print()
    print("=== LEAST 10 BORROWED BOOKS ===")

    least_borrowed = (
        transactions
        .groupby("book_id")
        .size()
        .sort_values(ascending=True)
        .head(10)
    )

    print(least_borrowed)

    print()
    print("=== BASIC KPI SUMMARY ===")

    kpis = {
        "total_transactions": len(transactions),
        "unique_books_borrowed": transactions["book_id"].nunique(),
        "unique_borrowers": transactions["borrower_id"].nunique(),
        "return_rate_pct": round(returned_count / len(transactions) * 100, 2),
        "avg_fine_per_transaction": round(average_fine, 2),
        "total_fine_collected": round(total_fine, 2),
    }

    for k, v in kpis.items():
        print(f"{k}: {v}")

    print()
    print("=== PREPARING CLEAN ANALYSIS DATASET ===")

    clean_df = merged.copy()
    clean_df["is_returned"] = clean_df["return_date"].notna()
    clean_df["fine"] = clean_df["fine"].fillna(0)

    output_path = BASE_DIR / "data" / "clean_analysis_dataset.csv"
    clean_df.to_csv(output_path, index=False)
    print(f"Clean dataset saved to: {output_path}")

    connection.close()


    print("All datasets loaded successfully.") 
    print()

    print("Transactions:", transactions.shape)
    print("Books:", books.shape)
    print("Borrowers:", borrowers.shape)
    print()
   
   
    print("=== CHART 1: TOP 10 MOST BORROWED BOOKS ===")

    top_books = (
        transactions
        .groupby("book_id")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    top_books.plot(kind="bar")

    plt.title("Top 10 Most Borrowed Books")
    plt.xlabel("Book ID")
    plt.ylabel("Number of Borrowings")
    plt.tight_layout()
    plt.show()


    print()
    print("=== CHART 2: BORROWINGS BY CATEGORY ===")

    merged = transactions.merge(books[["book_id", "category"]], on="book_id", how="left")

    category_counts = (
        merged
        .groupby("category")
        .size()
        .sort_values(ascending=False)
    )

    category_counts.plot(kind="bar")

    plt.title("Borrowings by Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Borrowings")
    plt.tight_layout()
    plt.show()


    print()
    print("=== CHART 3: MONTHLY BORROWING TREND ===")

    transactions["borrow_date"] = pd.to_datetime(transactions["borrow_date"])
    transactions["borrow_month"] = transactions["borrow_date"].dt.to_period("M")

    monthly_trend = (
        transactions
        .groupby("borrow_month")
        .size()
        .sort_index()
    )

    monthly_trend.index = monthly_trend.index.astype(str)
    monthly_trend.plot(kind="line", marker="o")

    plt.title("Monthly Borrowing Trend")
    plt.xlabel("Month")
    plt.ylabel("Number of Borrowings")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


    print()
    print("=== CHART 4: RETURNED VS NOT RETURNED ===")

    return_status = pd.Series(
        [returned_count, not_returned_count],
        index=["Returned", "Not Returned"]
    )

    return_status.plot(kind="pie", autopct="%1.1f%%", ylabel="")

    plt.title("Returned vs Not Returned")
    plt.tight_layout()
    plt.show()


    print()
    print("=== CHART 5: FINE BY CATEGORY ===")

    fine_by_category_total = (
        merged
        .groupby("category")["fine"]
        .sum()
        .sort_values(ascending=False)
    )

    fine_by_category_total.plot(kind="bar")

    plt.title("Total Fine by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Fine")
    plt.tight_layout()
    plt.show()


    print()
    print("=== CHART 6: TOP 10 ACTIVE BORROWERS ===")

    top_borrowers = (
        transactions
        .groupby("borrower_id")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    top_borrowers.plot(kind="bar")

    plt.title("Top 10 Active Borrowers")
    plt.xlabel("Borrower ID")
    plt.ylabel("Number of Borrowings")
    plt.tight_layout()
    plt.show()



    # Export cleaned transaction data for Excel and Power BI
    output_path = BASE_DIR / "data" / "library_analysis.csv"

    transactions.to_csv(output_path, index=False)

    print()
    print("Analysis dataset exported successfully.")
    print(f"Saved to: {output_path}")




if __name__ == "__main__":
    main()


