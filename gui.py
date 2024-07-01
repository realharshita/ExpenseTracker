import tkinter as tk
from tkinter import ttk, messagebox
from expense_manager import ExpenseManager
from report_manager import ReportManager

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        
        self.expense_manager = ExpenseManager()
        self.report_manager = ReportManager(self.expense_manager)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frames
        self.add_expense_frame = ttk.Frame(self.root, padding="10")
        self.add_expense_frame.grid(row=0, column=0, padx=10, pady=10)

        self.view_expense_frame = ttk.Frame(self.root, padding="10")
        self.view_expense_frame.grid(row=1, column=0, padx=10, pady=10)

        self.report_frame = ttk.Frame(self.root, padding="10")
        self.report_frame.grid(row=2, column=0, padx=10, pady=10)

        self.create_add_expense_widgets()
        self.create_view_expense_widgets()
        self.create_report_widgets()
        self.refresh_expenses()

    def create_add_expense_widgets(self):
        # Labels and Entries
        self.date_label = ttk.Label(self.add_expense_frame, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0, sticky=tk.W)
        self.date_entry = ttk.Entry(self.add_expense_frame)
        self.date_entry.grid(row=0, column=1)

        self.category_label = ttk.Label(self.add_expense_frame, text="Category:")
        self.category_label.grid(row=1, column=0, sticky=tk.W)
        self.category_entry = ttk.Entry(self.add_expense_frame)
        self.category_entry.grid(row=1, column=1)

        self.amount_label = ttk.Label(self.add_expense_frame, text="Amount:")
        self.amount_label.grid(row=2, column=0, sticky=tk.W)
        self.amount_entry = ttk.Entry(self.add_expense_frame)
        self.amount_entry.grid(row=2, column=1)

        self.description_label = ttk.Label(self.add_expense_frame, text="Description:")
        self.description_label.grid(row=3, column=0, sticky=tk.W)
        self.description_entry = ttk.Entry(self.add_expense_frame)
        self.description_entry.grid(row=3, column=1)

        self.add_button = ttk.Button(self.add_expense_frame, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

    def create_view_expense_widgets(self):
        self.expenses_listbox = tk.Listbox(self.view_expense_frame, width=80, height=15)
        self.expenses_listbox.grid(row=0, column=0, pady=10)

        self.delete_button = ttk.Button(self.view_expense_frame, text="Delete Selected Expense", command=self.delete_expense)
        self.delete_button.grid(row=1, column=0, pady=10)

    def create_report_widgets(self):
        self.report_text = tk.Text(self.report_frame, width=80, height=15)
        self.report_text.grid(row=0, column=0, pady=10)

        self.monthly_report_button = ttk.Button(self.report_frame, text="Generate Monthly Report", command=self.generate_monthly_report)
        self.monthly_report_button.grid(row=1, column=0, pady=5)

        self.category_report_button = ttk.Button(self.report_frame, text="Generate Category-wise Report", command=self.generate_category_report)
        self.category_report_button.grid(row=2, column=0, pady=5)

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        description = self.description_entry.get()

        if not date or not category or not amount:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        if not self.expense_manager.validate_date_format(date):
            messagebox.showerror("Error", "Please enter a valid date in YYYY-MM-DD format.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return

        new_expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }

        self.expense_manager.add_expense(new_expense)
        messagebox.showinfo("Success", "Expense added successfully.")
        self.refresh_expenses()
        self.clear_entries()

    def view_expenses(self):
        self.expenses_listbox.delete(0, tk.END)
        expenses = self.expense_manager.get_expenses()
        for index, expense in enumerate(expenses, start=1):
            expense_str = f"{index}. Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}"
            self.expenses_listbox.insert(tk.END, expense_str)

    def delete_expense(self):
        selected_index = self.expenses_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an expense to delete.")
            return

        index = selected_index[0]
        self.expense_manager.delete_expense(index)
        messagebox.showinfo("Success", "Expense deleted successfully.")
        self.refresh_expenses()

    def generate_monthly_report(self):
        report = self.report_manager.generate_monthly_report()
        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(tk.END, report)

    def generate_category_report(self):
        report = self.report_manager.generate_category_report()
        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(tk.END, report)

    def refresh_expenses(self):
        self.view_expenses()

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
