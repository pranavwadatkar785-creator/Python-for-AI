try:
    with open("Notes.txt", "r") as file:
        notes = file.read().splitlines()
    
except FileNotFoundError:
    with open("Notes.txt", "x") as file:
        pass
    notes = []

def save_notes():
    with open("Notes.txt", "w") as file:
        file.write("\n".join(notes))

def add_note():
    note = input("Enter your note: ")
    notes.append(note)
    save_notes()

def view_notes():
    if not notes:
        print("No notes available.")
    else:
        for i in notes:
            print(i)

def delete_note():
    view_notes()
    note_to_delete = input("Enter the note you want to delete: ")
    if note_to_delete in notes:
        notes.remove(note_to_delete)
        save_notes()
        print("Note deleted.")
    else:
        print("Note not found.")


while True:
    task = input("Choose an option:\n1. Add Note\n2. View Notes\n3. Delete Note\n4. Exit\nEnter your choice: ")
    if task == "1":
        add_note()
    elif task == "2":
        view_notes()
    elif task == "3":
        delete_note()
    elif task == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid Input")