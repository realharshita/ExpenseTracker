from data_manager import initialize_json, load_data, save_data
from expense_manager import add_expense, view_expenses, delete_expense
from report_manager import generate_monthly_report, generate_category_report

def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Generate Reports")
    print("5. Exit")

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
