# Library Management System

A simple **console-based Library Management System** built with **Python** and **Object-Oriented Programming (OOP)**.

The program allows users to add books, borrow and return books, search for books, and display all books in the library.

## Features

- Add a new book
- Prevent duplicate book IDs
- Borrow a book
- Return a borrowed book
- Search for a book by ID
- Display all books
- Show whether a book is available or borrowed
- Interactive command-line menu
- Uses Python classes and a dictionary to manage book records

## Technologies Used

- **Python 3**
- **Object-Oriented Programming (OOP)**
- **Python Dictionary**
- **Command-Line Interface (CLI)**

No external libraries or database are required.

## Project Structure

```text
Library-Management-System/
├── main.py
└── README.md
```

## How the Program Works

The project uses two main classes: `Book` and `Library`.

### `Book` Class

The `Book` class represents an individual book.

Each book contains:

- `book_id` — Unique ID of the book
- `title` — Book title
- `author` — Book author
- `available` — Indicates whether the book is available

A new book is initially marked as available:

```python
self.available = True
```

The class provides three main methods:

| Method | Purpose |
|---|---|
| `Borrow()` | Borrows the book if it is available |
| `Return()` | Returns the book if it is currently borrowed |
| `Display()` | Displays the book's details and status |

## `Library` Class

The `Library` class manages all books in the system.

Books are stored in a dictionary:

```python
self.books = {}
```

The book ID is used as the dictionary key.

| Method | Purpose |
|---|---|
| `ADD()` | Adds a new book |
| `search()` | Searches for a book by ID |
| `Book_Borrow()` | Borrows a book |
| `book_Return()` | Returns a book |
| `display_all()` | Displays all books |
| `Menu()` | Runs the main menu |

## Available Operations

When the program starts, the following menu is displayed:

```text
===============Library Management System=====================
1.Add book
2.Borrow book
3.Return book
4.Search book
5.Display books
6.Exit
=============================================================
```

### 1. Add Book

The user enters:

- Book ID
- Book title
- Author name

The program checks whether the book ID already exists. If it does, the book is not added.

### 2. Borrow Book

The user enters a book ID. If the book is available, its status changes to borrowed. If it has already been borrowed, the program reports that it is unavailable.

### 3. Return Book

The user enters a book ID. If the book is currently borrowed, it becomes available again.

### 4. Search Book

The user enters a book ID. If the book exists, its details and current status are displayed.

Example:

```text
Book Id: 101
Book Title: Python Basics
Auther: John Smith
Status: Available
```

### 5. Display Books

Displays all books currently stored in the library. If there are no books, the program displays:

```text
No book available!
```

### 6. Exit

Selecting option `6` exits the program.

## Example Workflow

```text
1. Add a book
       ↓
2. Search for the book
       ↓
3. Borrow the book
       ↓
4. Book status changes to Borrowed
       ↓
5. Return the book
       ↓
6. Book status changes back to Available
```

## Running the Project

### Prerequisites

Make sure **Python 3** is installed.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

### Clone the Repository

```bash
git clone https://github.com/fadifadifadifadifadi157-glitch/Library-Management-System.git
```

Go to the project directory:

```bash
cd Library-Management-System
```

### Run the Program

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

## Data Storage

The current version stores books in a Python dictionary:

```python
self.books = {}
```

This is **in-memory storage**. The program does not currently use a database or file-based storage, so all book records are lost when the program is closed.

## Code Concepts Demonstrated

This project demonstrates:

- Python classes and objects
- Constructors
- Instance attributes
- Methods
- Dictionaries
- Conditional statements
- Loops
- User input
- Object interaction
- Menu-driven programming

## Current Limitations

The current implementation is a simple beginner-level console application. Some limitations include:

- Book data is not permanently stored.
- There is no database integration.
- Input validation is limited.
- Entering a non-integer menu choice can cause a `ValueError`.
- There is no user/member management system.
- There are no due dates or return deadlines.
- There is no fine calculation.
- Search is currently based on book ID only.
- There is no automated test suite.
- There is no graphical user interface.

## Future Improvements

Possible improvements include:

- Add SQLite or PostgreSQL database support
- Add library member management
- Add book due dates and fine calculation
- Search books by title or author
- Add input validation and exception handling
- Add book categories
- Add borrowing history
- Add authentication and user roles
- Build a GUI using Tkinter or PyQt
- Build a web version using Flask or Django
- Add unit tests
- Add persistent storage using JSON or CSV

## Repository

GitHub repository:

https://github.com/fadifadifadifadifadi157-glitch/Library-Management-System

## Author
**Fowad Ajmal**

## License

No license is currently specified in the project.
