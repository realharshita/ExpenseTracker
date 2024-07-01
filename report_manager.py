from collections import defaultdict
from datetime import datetime

class ReportManager:
    def __init__(self, expense_manager):
        self.expense_manager = expense_manager

    def generate_monthly_report(self):
        report_lines = []
        monthly_expenses = defaultdict(float)
        expenses = self.expense_manager.get_expenses()
        
        for expense in expenses:
            expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
            month_year = expense_date.strftime("%B %Y")
            monthly_expenses[month_year] += expense["amount"]

        if monthly_expenses:
            report_lines.append("Monthly Spending Report:\n")
            for month_year, total in monthly_expenses.items():
                report_lines.append(f"{month_year}: ${total:.2f}\n")
        else:
            report_lines.append("No expenses found for reporting.\n")

        return "".join(report_lines)

    def generate_category_report(self):
        report_lines = []
        category_expenses = defaultdict(float)
        expenses = self.expense_manager.get_expenses()

        for expense in expenses:
            category_expenses[expense["category"]] += expense["amount"]

        if category_expenses:
            report_lines.append("Category-wise Spending Report:\n")
            for category, total in category_expenses.items():
                report_lines.append(f"{category}: ${total:.2f}\n")
        else:
            report_lines.append("No expenses found for reporting.\n")

        return "".join(report_lines)
