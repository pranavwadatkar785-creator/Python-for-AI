import json

File = "libdb.json"

try:
    with open(File,"r") as f:
        lib = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    lib={}

def save_library():
    with open(File,"w") as f:
        json.dump(lib, f, indent=4)

def add_book():
    name=input("Enter Book name: ")
    author=input("Enter Author name: ")
    year=input("Enter published year: ")

    lib[name]={
        "Author":author,
        "Year":year
    }
    save_library()

def update_book():
    name = input("Enter Book name: ")

    author=input("Enter Author name: ")
    year=input("Enter published year: ")

    if name in lib:
        lib[name]={
            "Author":author,
            "Year":year
        }
        save_library()
    else:
        print("Book not in library.")

def book_details():
    name = input("Enter Book Name: ")

    if name in lib:
        print(lib[name])
    else:
        print("Book Not in Library.")

def all_books():
    for book in lib:
        print(book)

def everything():
    for book,details in lib.items():
        print(book)
        print(details)
        print("-"*20)

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Get Book Details")
    print("4. Get All Books")
    print("5. Get Everything")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        update_book()

    elif choice == "3":
        book_details()

    elif choice == "4":
        all_books()

    elif choice == "5":
        everything()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")