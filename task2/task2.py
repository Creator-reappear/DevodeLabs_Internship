import csv
import os
from datetime import datetime

# Configuration
DATA_FILE = "expenses.csv"
CATEGORIES = ["Food", "Transport", "Shopping", "Entertainment", "Bills", "Other"]

def initialize_file():
    """Creates the CSV file with headers if it does not exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    """Prompts the user to enter and save a new expense entry."""
    print("\n--- ➕ Add New Expense ---")
    
    # 1. Date Input
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date_input:
        date_str = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            date_str = datetime.strptime(date_input, "%Y-%m-%d").strftime('%Y-%m-%d')
        except ValueError:
            print("❌ Invalid date format. Using today's date instead.")
            date_str = datetime.today().strftime('%Y-%m-%d')

    # 2. Category Selection
    print("\nAvailable Categories:")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f" {idx}. {cat}")
        
    try:
        cat_choice = int(input("Select category number: "))
        if 1 <= cat_choice <= len(CATEGORIES):
            category = CATEGORIES[cat_choice - 1]
        else:
            raise ValueError
    except ValueError:
        print("⚠️ Invalid choice. Defaulting to 'Other'.")
        category = "Other"

    # 3. Amount Input
    try:
        amount = float(input("Enter amount spent (€/$): "))
        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return
    except ValueError:
        print("❌ Invalid amount entry. Must be a valid number.")
        return

    # 4. Description
    description = input("Enter a brief description: ").strip()
    if not description:
        description = "N/A"

    # Save to File
    with open(DATA_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date_str, category, amount, description])
    
    print(f"✅ Success: Logged {amount} under '{category}'!")

def view_expenses():
    """Reads and prints all recorded rows from the file."""
    print("\n--- 📋 Expense History ---")
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        print("No expenses recorded yet.")
        return

    with open(DATA_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        
        has_data = False
        for idx, row in enumerate(reader, 1):
            has_data = True
            print(f"{idx}. [{row[0]}] {row[1]}: ${row[2]} — {row[3]}")
            
        if not has_data:
            print("No expenses recorded yet.")

def view_summary():
    """Calculates aggregate metrics and prints a spending summary."""
    print("\n--- 📊 Spending Summary ---")
    if not os.path.exists(DATA_FILE):
        print("No metrics available.")
        return

    total_spending = 0.0
    category_totals = {cat: 0.0 for cat in CATEGORIES}

    with open(DATA_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        
        for row in reader:
            try:
                amt = float(row[2])
                cat = row[1]
                total_spending += amt
                if cat in category_totals:
                    category_totals[cat] += amt
                else:
                    category_totals["Other"] += amt
            except (ValueError, IndexError):
                continue

    print(f"💰 Grand Total Spent: ${total_spending:.2f}\n")
    print("Breakdown by Category:")
    for cat, amt in category_totals.items():
        if amt > 0:
            percentage = (amt / total_spending) * 100 if total_spending > 0 else 0
            print(f" 🔹 {cat}: ${amt:.2f} ({percentage:.1f}%)")

def main():
    """Orchestrates main application loop."""
    initialize_file()
    
    while True:
        print("\n==============================")
        print("💸 PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. ➕ Add Expense")
        print("2. 📋 View Expenses")
        print("3. 📊 View Summary")
        print("4. ❌ Exit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            print("\nGoodbye! Stay on budget. 👋")
            break
        else:
            print("⚠️ Invalid choice. Please pick an option between 1 and 4.")

if __name__ == "__main__":
    main()
