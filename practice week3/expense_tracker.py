import json

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    expenses = {}

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    date = input("Enter expense date (DD-MM-YYYY): ")
    expenses[name] = {
        "Amount": amount,
        "Date": date
    }
    save_expenses()

def view_expenses():
    expense_name = input("Enter expense name to view details: ")
    if expense_name not in expenses:
        print("Expense not found.")
    else:
        print(expenses[expense_name])

def view_all_expenses():
    for expense, details in expenses.items():
        print(f"Expense: {expense}")
        print(f"Amount: {details['Amount']}")
        print(f"Date: {details['Date']}")
        print("-" * 20)


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expense Details")
    print("3. View All Expenses")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_all_expenses()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

