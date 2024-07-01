import tkinter as tk
from tkinter import messagebox, ttk
from data_manager import initialize_json, load_data, save_data
from expense_manager import add_expense, view_expenses, delete_expense
from report_manager import generate_monthly_report, generate_category_report

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("600x400")

        self.data_file = "expenses.json"
        initialize_json(self.data_file)
        self.data = load_data(self.data_file)

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        self.add_expense_frame = ttk.Frame(self.notebook)
        self.view_expense_frame = ttk.Frame(self.notebook)
        self.report_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.add_expense_frame, text='Add Expense')
        self.notebook.add(self.view_expense_frame, text='View Expenses')
        self.notebook.add(self.report_frame, text='Reports')

        self.create_add_expense_widgets()
        self.create_view_expense_widgets()
        self.create_report_widgets()

    def create_add_expense_widgets(self):
        self.date_label = ttk.Label(self.add_expense_frame, text="Date (YYYY-MM-DD):")
        self.date_label.pack(pady=5)
        self.date_entry = ttk.Entry(self.add_expense_frame)
        self.date_entry.pack(pady=5)

        self.category_label = ttk.Label(self.add_expense_frame, text="Category:")
        self.category_label.pack(pady=5)
        self.category_entry = ttk.Entry(self.add_expense_frame)
        self.category_entry.pack(pady=5)

        self.amount_label = ttk.Label(self.add_expense_frame, text="Amount:")
        self.amount_label.pack(pady=5)
        self.amount_entry = ttk.Entry(self.add_expense_frame)
        self.amount_entry.pack(pady=5)

        self.description_label = ttk.Label(self.add_expense_frame, text="Description (optional):")
        self.description_label.pack(pady=5)
        self.description_entry = ttk.Entry(self.add_expense_frame)
        self.description_entry.pack(pady=5)

        self.add_button = ttk.Button(self.add_expense_frame, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=10)



if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
