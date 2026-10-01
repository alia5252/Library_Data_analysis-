import csv
import random
from datetime import date, timedelta
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
random.seed(42)
START_DATE = date(2025, 1, 1)
END_DATE = date(2026, 12, 31)

book_templates = [
    ("Introduction to Quantum Mechanics", "David J. Griffiths", "Physics"),
    ("Classical Mechanics", "John R. Taylor", "Physics"),
    ("Introduction to Electrodynamics", "David J. Griffiths", "Physics"),
    ("Modern Physics", "Kenneth S. Krane", "Physics"),
    ("Solid State Physics", "Neil W. Ashcroft", "Physics"),

    ("Mathematical Methods for Physicists", "Arfken", "Mathematics"),
    ("Advanced Engineering Mathematics", "Erwin Kreyszig", "Mathematics"),
    ("Linear Algebra", "Gilbert Strang", "Mathematics"),
    ("Complex Analysis", "James Ward Brown", "Mathematics"),
    ("Differential Equations", "Dennis G. Zill", "Mathematics"),

    ("Python Crash Course", "Eric Matthes", "Computer Science"),
    ("Introduction to Algorithms", "Cormen et al.", "Computer Science"),
    ("Computer Networks", "Andrew S. Tanenbaum", "Computer Science"),
    ("Operating System Concepts", "Silberschatz", "Computer Science"),
    ("Database System Concepts", "Korth", "Computer Science"),

    ("Microelectronic Circuits", "Sedra and Smith", "Electronics"),
    ("Electronic Devices", "Thomas L. Floyd", "Electronics"),
    ("Digital Logic Design", "M. Morris Mano", "Electronics"),
    ("Communication Systems", "Simon Haykin", "Electronics"),
    ("Signals and Systems", "Alan V. Oppenheim", "Electronics"),

    ("Physical Chemistry", "Atkins", "Chemistry"),
    ("Organic Chemistry", "Morrison and Boyd", "Chemistry"),
    ("Inorganic Chemistry", "J. D. Lee", "Chemistry"),
    ("Analytical Chemistry", "Skoog", "Chemistry"),
    ("Thermodynamics", "P. K. Nag", "Chemistry"),

    ("Cell Biology", "Bruce Alberts", "Biology"),
    ("Molecular Biology of the Cell", "Alberts et al.", "Biology"),
    ("Genetics", "Benjamin A. Pierce", "Biology"),
    ("Ecology", "Michael Begon", "Biology"),
    ("Human Physiology", "Guyton", "Biology"),

    ("Engineering Mechanics", "S. Timoshenko", "Engineering"),
    ("Fluid Mechanics", "Frank M. White", "Engineering"),
    ("Heat Transfer", "J. P. Holman", "Engineering"),
    ("Control Systems", "Ogata", "Engineering"),
    ("Engineering Materials", "Callister", "Engineering"),

    ("Introduction to Statistics", "Walpole", "Statistics"),
    ("Probability and Statistics", "DeGroot", "Statistics"),
    ("Statistical Inference", "Casella and Berger", "Statistics"),
    ("Applied Statistics", "David C. Howell", "Statistics"),
    ("Regression Analysis", "Montgomery", "Statistics"),
]
books = []

for book_id, (title, author, category) in enumerate(book_templates, start=1):
    books.append(
        {
            "book_id": book_id,
            "title": title,
            "author": author,
            "category": category,
            "quantity": random.randint(2, 8),
        }
    )
    
#Genrate Borrower Data

borrower_names = [
    "Aarav Patel",
    "Priya Shah",
    "Rahul Mehta",
    "Ananya Desai",
    "Arjun Joshi",
    "Neha Patel",
    "Rohan Shah",
    "Isha Mehta",
    "Kunal Desai",
    "Sneha Joshi",
    "Aditya Patel",
    "Pooja Shah",
    "Vivek Mehta",
    "Kavya Desai",
    "Yash Joshi",
    "Riya Patel",
    "Harsh Shah",
    "Nisha Mehta",
    "Dev Desai",
    "Aditi Joshi",
    "Manav Patel",
    "Simran Shah",
    "Nikhil Mehta",
    "Diya Desai",
    "Akash Joshi",
    "Meera Patel",
    "Sahil Shah",
    "Tanya Mehta",
    "Dhruv Desai",
    "Mahi Joshi",
    "Kabir Patel",
    "Riya Shah",
    "Parth Mehta",
    "Avni Desai",
    "Jay Joshi",
    "Shreya Patel",
    "Mihir Shah",
    "Tanvi Mehta",
    "Om Desai",
    "Khushi Joshi",
    "Dev Patel",
    "Mansi Shah",
    "Yuvraj Mehta",
    "Ira Desai",
    "Aman Joshi",
    "Palak Patel",
    "Krish Shah",
    "Jhanvi Mehta",
    "Darsh Desai",
    "Anushka Joshi",
    "Rudra Patel",
    "Nandini Shah",
    "Samar Mehta",
    "Aarohi Desai",
    "Ved Joshi",
    "Ishita Patel",
    "Parth Shah",
    "Ritesh Mehta",
    "Myra Desai",
    "Aryan Joshi",
    "Sakshi Patel",
    "Varun Shah",
    "Komal Mehta",
    "Reyansh Desai",
    "Riddhi Joshi",
    "Atharv Patel",
    "Bhavya Shah",
    "Manish Mehta",
    "Ayesha Desai",
    "Kartik Joshi",
    "Pallavi Patel",
    "Naman Shah",
    "Shruti Mehta",
    "Vivaan Desai",
    "Anjali Joshi",
    "Raghav Patel",
    "Payal Shah",
    "Mohit Mehta",
    "Rhea Desai",
    "Abhishek Joshi",
    "Sanya Patel",
    "Varsha Shah",
    "Siddharth Mehta",
    "Navya Desai",
    "Aaryan Joshi",
    "Ishaan Patel",
    "Naina Shah",
    "Manav Mehta",
    "Roshni Desai",
    "Karan Joshi",
    "Muskan Patel",
    "Yash Shah",
    "Shivam Mehta",
    "Anvi Desai",
    "Advik Joshi",
    "Poonam Patel",
    "Raj Shah",
    "Tina Mehta",
    "Vihaan Desai",
    "Ritika Joshi",
]

borrowers = []

for student_number, borrower_name in enumerate(borrower_names, start=1):
    borrowers.append(
        {
            "borrower_id": f"STU{student_number:03d}",
            "borrower_name": borrower_name,
        }
    )


def random_date(start_date, end_date):
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    return start_date + timedelta(days=random_days)

def generate_transactions():
    transactions = []

    for borrow_id in range(1, 1001):
        book = random.choice(books)
        borrower = random.choice(borrowers)

        borrow_date = random_date(START_DATE, END_DATE)

        due_date = borrow_date + timedelta(days=14)

        return_date = due_date + timedelta(
            days=random.randint(-3, 14)
        )

        if return_date <= due_date:
            fine = 0
        else:
            late_days = (return_date - due_date).days
            fine = late_days * 5

        returned = 1

        transactions.append(
            {
                "borrow_id": borrow_id,
                "book_id": book["book_id"],
                "borrower_id": borrower["borrower_id"],
                "borrow_date": borrow_date.isoformat(),
                "due_date": due_date.isoformat(),
                "return_date": return_date.isoformat(),
                "fine": fine,
                "returned": returned,
            }
        )

    return transactions

def save_transactions(transactions):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    file_path = DATA_DIR / "borrow_transactions.csv"

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "borrow_id",
                "book_id",
                "borrower_id",
                "borrow_date",
                "due_date",
                "return_date",
                "fine",
                "returned",
            ],
        )

        writer.writeheader()
        writer.writerows(transactions)

    print(f"Transactions saved to: {file_path}")

def generate_transactions():
    transactions = []

    start_date = date(2025, 1, 1)
    end_date = date(2026, 12, 31)

    # Make some books more popular than others.
    book_weights = []

    for book in books:
        if book["category"] in ["Physics", "Computer Science", "Mathematics"]:
            weight = 5
        elif book["category"] in ["Electronics", "Engineering", "Statistics"]:
            weight = 3
        else:
            weight = 2

        book_weights.append(weight)

    for transaction_id in range(1, 1001):
        # Random borrowing date
        days_range = (end_date - start_date).days
        borrow_date = start_date + timedelta(
            days=random.randint(0, days_range)
        )

        # Select a book using popularity weights
        book = random.choices(
            books,
            weights=book_weights,
            k=1,
        )[0]

        # Select a borrower
        borrower = random.choice(borrowers)

        # Standard borrowing period: 14 days
        due_date = borrow_date + timedelta(days=14)

        # Decide whether the book has been returned
        returned = random.choices(
            [True, False],
            weights=[92, 8],
            k=1,
        )[0]

        if returned:
            return_type = random.choices(
                ["on_time", "late", "very_late"],
                weights=[75, 20, 5],
                k=1,
            )[0]

            if return_type == "on_time":
                return_date = due_date - timedelta(
                    days=random.randint(0, 3)
                )

            elif return_type == "late":
                return_date = due_date + timedelta(
                    days=random.randint(1, 10)
                )

            else:
                return_date = due_date + timedelta(
                    days=random.randint(11, 30)
                )

            late_days = max(
                0,
                (return_date - due_date).days
            )

            # ₹2 fine per late day
            fine = late_days * 2

        else:
            return_date = None
            fine = 0

        transactions.append(
            {
                "borrow_id": f"BR{transaction_id:04d}",
                "book_id": book["book_id"],
                "borrower_id": borrower["borrower_id"],
                "borrow_date": borrow_date.isoformat(),
                "due_date": due_date.isoformat(),
                "return_date": (
                    return_date.isoformat()
                    if return_date
                    else ""
                ),
                "fine": fine,
                "returned": returned,
            }
        )

    return transactions

def save_transactions(transactions):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    file_path = DATA_DIR / "borrow_transactions.csv"

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "borrow_id",
                "book_id",
                "borrower_id",
                "borrow_date",
                "due_date",
                "return_date",
                "fine",
                "returned",
            ],
        )

        writer.writeheader()
        writer.writerows(transactions)

    print(f"Transactions saved to: {file_path}")

def save_books():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    file_path = DATA_DIR / "books.csv"

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["book_id", "title", "author", "category", "quantity"],
        )

        writer.writeheader()
        writer.writerows(books)

    print(f"Books saved to: {file_path}")


def save_borrowers():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    file_path = DATA_DIR / "borrowers.csv"

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["borrower_id", "borrower_name"],
        )

        writer.writeheader()
        writer.writerows(borrowers)

    print(f"Borrowers saved to: {file_path}")




save_books()
save_borrowers()

transactions = generate_transactions()
save_transactions(transactions)


