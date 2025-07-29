import sqlite3

def create_tables():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Create Books Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            BookID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT,
            Author TEXT,
            Year INTEGER,
            AvailableCopies INTEGER
        )
    ''')

    # Create Members Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Email TEXT,
            Phone TEXT,
            Address TEXT
        )
    ''')

    # Create Loans Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Loans (
            LoanID INTEGER PRIMARY KEY AUTOINCREMENT,
            MemberID INTEGER,
            BookID INTEGER,
            LoanDate TEXT,
            ReturnDate TEXT,
            FOREIGN KEY (MemberID) REFERENCES Members(MemberID),
            FOREIGN KEY (BookID) REFERENCES Books(BookID)
        )
    ''')

    conn.commit()
    conn.close()

create_tables()
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_issued = False

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

class Member:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.id = None

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.book_counter = 1
        self.member_counter = 1

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def display_books(self):
        print("\n===== Books =====")
        for book in self.books:
            print(book)

    def add_member(self, name, email, phone, address):
        member = Member(name, email, phone, address)
        member.id = self.member_counter
        self.members.append(member)
        self.member_counter += 1
        print(f"Member '{name}' added successfully!")

    def display_members(self):
        print("\n===== Member Details =====")
        for member in self.members:
            print(member)

    def issue_book(self, book_id, member_id):
        if book_id <= len(self.books) and member_id <= len(self.members):
            book = self.books[book_id - 1]
            member = self.members[member_id - 1]
            if not book.is_issued:
                book.is_issued = True
                print(f"\nBook '{book.title}' issued to {member.name} successfully!")
            else:
                print("\nError: Book is already issued.")
        else:
            print("\nError: Invalid book or member ID.")

def main():
    library = Library()

    while True:
        print("\n===== Library Management Menu =====")
        print("1. Books")
        print("2. Member Details")
        print("3. Issue Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            library.display_books()
            if input("\nDo you want to add a new book? (y/n): ").lower() == 'y':
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                year = input("Enter publication year: ")
                library.add_book(title, author, year)

        elif choice == '2':
            library.display_members()
            if input("\nDo you want to add a new member? (y/n): ").lower() == 'y':
                name = input("Enter member name: ")
                email = input("Enter member email: ")
                phone = input("Enter member phone: ")
                address = input("Enter member address: ")
                library.add_member(name, email, phone, address)

        elif choice == '3':
            book_id = int(input("\nEnter book ID to issue: "))
            member_id = int(input("Enter member ID: "))
            library.issue_book(book_id, member_id)

        elif choice == '4':
            print("\nExiting the system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()

