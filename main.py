import json
import os

def initialize_json(file):
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump({"expenses": []}, f)
        print("Initialized expenses.json")

def load_data(file):
    with open(file, 'r') as f:
        return json.load(f)

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

def add_expense(data):
    print("\nAdding Expense:")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description (optional): ")

    new_expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    data["expenses"].append(new_expense)
    print("Expense added successfully.")

def view_expenses(data):
    print("\nViewing Expenses:")
    if not data["expenses"]:
        print("No expenses added yet.")
    else:
        for index, expense in enumerate(data["expenses"], start=1):
            print(f"\nExpense {index}:")
            print(f"Date: {expense['date']}")
            print(f"Category: {expense['category']}")
            print(f"Amount: {expense['amount']}")
            print(f"Description: {expense['description']}")

def delete_expense(data):
    print("\nDeleting Expense:")
    if not data["expenses"]:
        print("No expenses to delete.")
        return

    view_expenses(data)
    choice = input("Enter the index of the expense to delete (0 to cancel): ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(data["expenses"]):
            deleted_expense = data["expenses"].pop(index)
            print(f"Deleted Expense: {deleted_expense}")
        else:
            print("Invalid index. No expense deleted.")
    except ValueError:
        print("Invalid input. No expense deleted.")

def main():
    json_file = "expenses.json"
    initialize_json(json_file)
    data = load_data(json_file)
    print("Welcome to the Expense Tracker")

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense(data)
        elif choice == '2':
            view_expenses(data)
        elif choice == '3':
            delete_expense(data)
        elif choice == '4':
            print("Exiting...")
            save_data(json_file, data)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
