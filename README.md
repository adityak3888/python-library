# Library Book Manager – Unit 2 Mini Project

This is a small **CLI-based Library Inventory & Borrowing System** written in Python for my BCA course.

It runs in the terminal and lets the user:

- Add new books to the library
- View all books in a table-style list
- Search books by ID or by title (substring match)
- Borrow a book for a student (copies reduced)
- Return a book (copies increased)
- See all borrowed books with a list comprehension
- Save all records to a text file (bonus)

## 🧠 Concepts Used

- Lists, dictionaries, sets and tuples  
- Functions (modular design)  
- Loops and conditionals (menu-driven `while` loop)  
- Recursion (to calculate total copies)  
- Lambda function for sorting book IDs  
- String formatting with f-strings, `\n`, `\t`  
- Basic file handling (`open`, `write`) for saving records

## ▶️ How to Run

1. Make sure Python is installed (`python --version`).
2. Save the file as **library.py** in a folder named `library_manager`.
3. Open terminal / command prompt inside that folder.
4. Run:

   ```bash
   python library.py
