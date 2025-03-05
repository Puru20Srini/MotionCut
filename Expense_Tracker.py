import csv
import os
from datetime import datetime

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# Expense categories
CATEGORIES = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]

def load_expenses():
    expenses = []
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    return expenses

def save_expenses(expenses):
    with open(EXPENSE_FILE, mode="w", newline="") as file:
        fieldnames = ["Date", "Amount", "Category", "Description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense():
    
    while True:
        try:
            amount = float(input("Enter the amount spent: "))
            if amount <= 0:
                print("Amount must be greater than 0. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("Select a category:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}. {category}")
    while True:
        try:
            category_choice = int(input("Enter the category number: "))
            if 1 <= category_choice <= len(CATEGORIES):
                category = CATEGORIES[category_choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid category number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    description = input("Enter a brief description: ")

    expense = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Amount": amount,
        "Category": category,
        "Description": description,
    }
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_monthly_summary():
    """Provide a summary of monthly expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    # Group expenses by month and category
    summary = {}
    for expense in expenses:
        date = datetime.strptime(expense["Date"], "%Y-%m-%d")
        month_year = date.strftime("%Y-%m")
        category = expense["Category"]
        amount = float(expense["Amount"])

        if month_year not in summary:
            summary[month_year] = {}
        if category not in summary[month_year]:
            summary[month_year][category] = 0
        summary[month_year][category] += amount

    print("\nMonthly Summary:")
    for month, categories in summary.items():
        print(f"\n{month}:")
        for category, total in categories.items():
            print(f"{category}: ${total:.2f}")

def view_category_summary():
    
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    # Group expenses by category
    summary = {}
    for expense in expenses:
        category = expense["Category"]
        amount = float(expense["Amount"])

        if category not in summary:
            summary[category] = 0
        summary[category] += amount

    print("\nCategory-wise Summary:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

def main():
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_monthly_summary()
        elif choice == "3":
            view_category_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()