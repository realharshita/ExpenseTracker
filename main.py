# main.py

import json
import os
from collections import defaultdict
from datetime import datetime

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
    print("4. Generate Reports")
    print("5. Exit")

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

def generate_monthly_report(data):
    print("\nGenerating Monthly Spending Report:")

    if not data["expenses"]:
        print("No expenses added yet.")
        return

    monthly_expenses = defaultdict(float)
    for expense in data["expenses"]:
        try:
            expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
            month_year = expense_date.strftime("%B %Y")
            monthly_expenses[month_year] += expense["amount"]
        except ValueError:
            print(f"Ignoring expense with invalid date format: {expense}")

    if monthly_expenses:
        print("Monthly Spending:")
        for month_year, total in monthly_expenses.items():
            print(f"{month_year}: ${total:.2f}")
    else:
        print("No valid expenses found for reporting.")

def generate_category_report(data):
    print("\nGenerating Category-wise Spending Report:")

    if not data["expenses"]:
        print("No expenses added yet.")
        return

    category_expenses = defaultdict(float)
    for expense in data["expenses"]:
        category_expenses[expense["category"]] += expense["amount"]

    if category_expenses:
        print("Category-wise Spending:")
        for category, total in category_expenses.items():
            print(f"{category}: ${total:.2f}")
    else:
        print("No expenses found for reporting.")

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
            print("\nReport Options:")
            print("1. Monthly Spending Report")
            print("2. Category-wise Spending Report")
            report_choice = input("Enter your report choice (0 to cancel): ")
            if report_choice == '1':
                generate_monthly_report(data)
            elif report_choice == '2':
                generate_category_report(data)
            elif report_choice == '0':
                continue
            else:
                print("Invalid choice. Please try again.")
        elif choice == '5':
            print("Exiting...")
            save_data(json_file, data)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
