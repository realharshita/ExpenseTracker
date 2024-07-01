from collections import defaultdict
from datetime import datetime

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
