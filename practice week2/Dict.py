dict = {"K1":"Pranav","K2":"Shravan"}
print(dict.get("K2")) #If key does not exists return None
print(dict.items(),":items")
print(dict.pop("K2"),":pop-> remove and return ")
print(dict.keys())
dict.update({"K2":"Shravan"})
print(dict)
print(dict.values())


lib={}
def add_book():
    book_name= input("Enter Book name: ")
    book_details=input("Enter Book details in list form: ")
    lib.update({book_name:book_details})
def update_book():
    book_to_update= input("Enter Book name to Update: ")
    details_updated=input("Enter Book updated details in list form: ")
    lib.update({book_to_update:details_updated})
def book_details():
    book = input("Enter Book Name to get details: ")
    if lib.get(book)==None:
        print("Book Does not Exist.")
    else:
        print(lib.get(book))
def all_books():
    print("All the Books in the LIbrary are: ",lib.keys())
def everthing():
    for i in lib:
        print(i)

def library_management_sys():
    
    while True:
        task = input("Add Book(1), Update Book(2), Get Book Details(3), Get all the Books(4), Get Everything(5), End(6): ")

        if task == "1":
            add_book()
        elif task == "2":
            update_book()
        elif task == "3":
           book_details() 
        elif task == "4":
            all_books()
        elif task =="5":
            everthing()
        elif task =="6":
            print("Ending Program...")
            break
        else:
            print("Invalid Input")

library_management_sys()