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

def main():
    json_file = "expenses.json"
    initialize_json(json_file)
    data = load_data(json_file)
    print("Welcome to the Expense Tracker")

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Add Expense selected")
            # Placeholder for add expense function
        elif choice == '2':
            print("View Expenses selected")
            # Placeholder for view expenses function
        elif choice == '3':
            print("Delete Expense selected")
            # Placeholder for delete expense function
        elif choice == '4':
            print("Exiting...")
            save_data(json_file, data)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
