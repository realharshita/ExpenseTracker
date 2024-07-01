import re
from datetime import datetime
import json

class ExpenseManager:
    def __init__(self):
        self.data_file = "expenses.json"
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"expenses": []}

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def validate_date_format(self, date):
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            try:
                datetime.strptime(date, "%Y-%m-%d")
                return True
            except ValueError:
                return False
        return False

    def add_expense(self, expense):
        self.data["expenses"].append(expense)
        self.save_data()

    def get_expenses(self):
        return self.data["expenses"]

    def delete_expense(self, index):
        del self.data["expenses"][index]
        self.save_data()
