from datetime import datetime

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def add_expense(data):
    print("\nAdding Expense:")
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")
        return

    category = input("Enter category: ")
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be a positive number.")
            return
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

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