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

    def create_view_expense_widgets(self):
        self.expenses_listbox = tk.Listbox(self.view_expense_frame, width=80, height=15)
        self.expenses_listbox.pack(pady=10)

        self.delete_button = ttk.Button(self.view_expense_frame, text="Delete Selected Expense", command=self.delete_expense)
        self.delete_button.pack(pady=10)

        self.refresh_expenses()

    def create_report_widgets(self):
        self.report_text = tk.Text(self.report_frame, width=80, height=15)
        self.report_text.pack(pady=10)

        self.monthly_report_button = ttk.Button(self.report_frame, text="Generate Monthly Report", command=self.generate_monthly_report)
        self.monthly_report_button.pack(pady=5)

        self.category_report_button = ttk.Button(self.report_frame, text="Generate Category-wise Report", command=self.generate_category_report)
        self.category_report_button.pack(pady=5)

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        description = self.description_entry.get()

        if not date or not category or not amount:
            messagebox.showerror("Error", "Please fill in all required fields.")
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

        self.data["expenses"].append(new_expense)
        save_data(self.data_file, self.data)
        messagebox.showinfo("Success", "Expense added successfully.")
        self.refresh_expenses()
        self.clear_entries()

    def view_expenses(self):
        self.expenses_listbox.delete(0, tk.END)
        for index, expense in enumerate(self.data["expenses"], start=1):
            expense_str = f"{index}. Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}"
            self.expenses_listbox.insert(tk.END, expense_str)

    def delete_expense(self):
        selected_index = self.expenses_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an expense to delete.")
            return

        index = selected_index[0]
        del self.data["expenses"][index]
        save_data(self.data_file, self.data)
        messagebox.showinfo("Success", "Expense deleted successfully.")
        self.refresh_expenses()

    def generate_monthly_report(self):
        self.report_text.delete(1.0, tk.END)
        report_lines = []
        monthly_expenses = defaultdict(float)
        for expense in self.data["expenses"]:
            expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
            month_year = expense_date.strftime("%B %Y")
            monthly_expenses[month_year] += expense["amount"]

        if monthly_expenses:
            report_lines.append("Monthly Spending Report:\n")
            for month_year, total in monthly_expenses.items():
                report_lines.append(f"{month_year}: ${total:.2f}\n")
        else:
            report_lines.append("No expenses found for reporting.\n")

        self.report_text.insert(tk.END, "".join(report_lines))

    def generate_category_report(self):
        self.report_text.delete(1.0, tk.END)
        report_lines = []
        category_expenses = defaultdict(float)
        for expense in self.data["expenses"]:
            category_expenses[expense["category"]] += expense["amount"]

        if category_expenses:
            report_lines.append("Category-wise Spending Report:\n")
            for category, total in category_expenses.items():
                report_lines.append(f"{category}: ${total:.2f}\n")
        else:
            report_lines.append("No expenses found for reporting.\n")

        self.report_text.insert(tk.END, "".join(report_lines))

    def refresh_expenses(self):
        self.view_expenses()

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
