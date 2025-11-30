# Name: Your Name
# Roll No: Your Roll No
# Course: BCA (Cyber Security)
# Semester: 1st
# Subject: Programming for Problem Solving using Python
# Assignment: Unit-2 – Library Inventory & Borrowing System
# Title: Library Book Manager CLI
# Date:

# -----------------------------
# Global Data Structures
# -----------------------------

# books:  { "B101": {"title": "...", "author": "...", "copies": 5}, ... }
books = {}

# borrowed: { "StudentName": "BookID", ... }
borrowed = {}


# -----------------------------
# Helper / Utility Functions
# -----------------------------

def print_welcome():
    print("=" * 50)
    print("          UNIVERSITY LIBRARY SYSTEM        ")
    print("=" * 50)


def print_menu():
    """Display main menu options."""
    print("\n------------- MAIN MENU -------------")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")
    print("-------------------------------------")


def add_book():
    """Task 2: Input and store book details."""
    print("\n--- Add New Book ---")
    book_id = input("Enter Book ID (e.g., B101): ").strip()

    if book_id in books:
        print("Book ID already exists. Cannot add duplicate.")
        return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    try:
        copies = int(input("Enter Number of Copies: "))
    except ValueError:
        print("Invalid number. Setting copies to 1 by default.")
        copies = 1

    books[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }

    print(f"Book '{title}' added successfully!")


def display_books():
    """Task 3: Display all books in tabular form."""
    if not books:
        print("\nNo books in library yet. Please add some books.")
        return

    print("\n----------------- BOOK LIST -----------------")
    print("ID\tTitle\t\tAuthor\t\tCopies")
    print("-" * 45)

    # Use lambda to sort books by ID for nicer output
    for book_id, info in sorted(books.items(), key=lambda x: x[0]):
        title = info["title"]
        author = info["author"]
        copies = info["copies"]
        print(f"{book_id}\t{title}\t\t{author}\t\t{copies}")

    print("-" * 45)

    # Small example of using set (unique authors)
    unique_authors = {details["author"] for details in books.values()}
    print("Unique authors in library:", ", ".join(unique_authors))


def search_by_id(book_id):
    """Search for a book using its ID. Returns tuple (found, info)."""
    if book_id in books:
        return True, books[book_id]
    return False, None


def search_by_title_substring(title_part):
    """
    Search by title substring (case-insensitive).
    Returns list of (book_id, book_info) tuples.
    """
    results = []
    for bid, info in books.items():
        if title_part.lower() in info["title"].lower():
            results.append((bid, info))
    return results


def search_book():
    """Task 3: Search book by ID or by title substring."""
    if not books:
        print("\nNo books available to search.")
        return

    print("\n--- Search Book ---")
    print("1. Search by Book ID")
    print("2. Search by Title (substring)")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        book_id = input("Enter Book ID: ").strip()
        found, info = search_by_id(book_id)
        if found:
            print("\nBook Found:")
            print(f"ID: {book_id}")
            print(f"Title: {info['title']}")
            print(f"Author: {info['author']}")
            print(f"Copies: {info['copies']}")
        else:
            print("Book Not Found.")
    elif choice == "2":
        title_sub = input("Enter part of the title: ").strip()
        results = search_by_title_substring(title_sub)
        if results:
            print("\nBooks Found:")
            for bid, info in results:
                print(f"{bid} -> {info['title']} by {info['author']} ({info['copies']} copies)")
        else:
            print("No books match that title.")
    else:
        print("Invalid choice.")


def borrow_book():
    """Task 4: Borrowing system."""
    if not books:
        print("\nNo books available to borrow.")
        return

    print("\n--- Borrow Book ---")
    student = input("Enter Student Name: ").strip()
    book_id = input("Enter Book ID to borrow: ").strip()

    # Check if book exists
    if book_id not in books:
        print("Book ID not found.")
        return

    # Check if copies available
    if books[book_id]["copies"] <= 0:
        print("No copies available for this book.")
        return

    # Check if student already borrowed a book (simple version)
    if student in borrowed:
        print(f"{student} has already borrowed Book ID: {borrowed[student]}")
        return

    # Borrow
    books[book_id]["copies"] -= 1
    borrowed[student] = book_id
    print(f"Book {book_id} issued to {student} successfully!")


def return_book():
    """Task 5: Return Book + List Comprehension for borrowed list."""
    if not borrowed:
        print("\nNo books are currently borrowed.")
        return

    print("\n--- Return Book ---")
    student = input("Enter Student Name: ").strip()
    book_id = input("Enter Book ID to return: ").strip()

    # Check if record exists
    if student in borrowed and borrowed[student] == book_id:
        books[book_id]["copies"] += 1          # increase copies
        del borrowed[student]                  # remove from borrowed dict
        print("Book returned successfully.")
    else:
        print("No matching borrow record found.")

    # Show all currently borrowed books using list comprehension
    if borrowed:
        borrowed_list = [f"{stu} -> {bid}" for stu, bid in borrowed.items()]
        print("\nCurrently borrowed books:")
        for entry in borrowed_list:
            print(entry)
    else:
        print("No books are currently borrowed.")


# Example of a small recursive function (to satisfy recursion requirement)
def total_copies_recursive(ids, index=0):
    """Return total copies of books whose IDs are in 'ids' list."""
    if index == len(ids):
        return 0
    book_id = ids[index]
    copies_here = books.get(book_id, {}).get("copies", 0)
    return copies_here + total_copies_recursive(ids, index + 1)


def save_to_file():
    """Bonus: Save current books and borrowed data to text file."""
    filename = "library_records.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("LIBRARY BOOK RECORDS\n")
        f.write("-" * 40 + "\n")
        for bid, info in books.items():
            line = f"{bid},{info['title']},{info['author']},{info['copies']}\n"
            f.write(line)

        f.write("\nBORROWED BOOKS\n")
        f.write("-" * 40 + "\n")
        for student, bid in borrowed.items():
            f.write(f"{student} -> {bid}\n")

    print(f"All records saved to {filename}")


# -----------------------------
# Main Program Loop (Task 6)
# -----------------------------

def main():
    print_welcome()

    # Pre-fill with a few sample books so you have at least 5 quickly (you can still add more)
    # Comment these out if teacher wants ONLY manual entry.
    sample_books = {
        "B101": {"title": "Python Basics", "author": "Guido", "copies": 3},
        "B102": {"title": "Data Structures", "author": "Cormen", "copies": 2},
        "B103": {"title": "Algorithms", "author": "Turing", "copies": 4},
        "B104": {"title": "Computer Networks", "author": "Tanenbaum", "copies": 1},
        "B105": {"title": "Operating Systems", "author": "Silberschatz", "copies": 2},
    }
    books.update(sample_books)

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            # optional: show total copies using recursion
            ids = list(books.keys())
            total = total_copies_recursive(ids)
            print(f"\nTotal copies of all books (using recursion): {total}")

            save = input("Do you want to save records to file? (yes/no): ").lower().strip()
            if save == "yes":
                save_to_file()
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1-6.")


# Run program
if __name__ == "__main__":
    main()
