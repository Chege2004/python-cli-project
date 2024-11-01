from models.user import User
from models.budget import Budget
from models.expense import Expense
from models.database import initialize_db

def main_menu():
    print("Welcome to Budget Tracker")
    while True:
        print("\nMain Menu:")
        print("1. Manage Users")
        print("2. Manage Budgets")
        print("3. Manage Expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            user_menu()
        elif choice == '2':
            budget_menu()
        elif choice == '3':
            expense_menu()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu():
    print("\nUser Management:")
    print("1. Add User")
    print("2. View All Users")
    
    choice = input("Choose an option: ")
    if choice == '1':
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        User.create_user(name, email)
        print("User created successfully.")
    elif choice == '2':
        users = User.get_all_users()
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    else:
        print("Invalid choice.")

def budget_menu():
    print("\nBudget Management:")
    print("1. Add Budget")
    print("2. View All Budgets")
    
    choice = input("Choose an option: ")
    if choice == '1':
        category = input("Enter budget category: ")
        limit = float(input("Enter budget limit: "))
        user_id = int(input("Enter user ID: "))
        Budget.create_budget(category, limit, user_id)
        print("Budget created successfully.")
    elif choice == '2':
        budgets = Budget.get_all_budgets()
        for budget in budgets:
            print(f"ID: {budget.id}, Category: {budget.category}, Limit: {budget.limit}")
    else:
        print("Invalid choice.")

def expense_menu():
    print("\nExpense Management:")
    print("1. Add Expense")
    print("2. View All Expenses")
    
    choice = input("Choose an option: ")
    if choice == '1':
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        budget_id = int(input("Enter budget ID: "))
        Expense.create_expense(description, amount, budget_id)
        print("Expense added successfully.")
    elif choice == '2':
        expenses = Expense.get_all_expenses()
        for expense in expenses:
            print(f"ID: {expense.id}, Description: {expense.description}, Amount: {expense.amount}")
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    initialize_db()
    main_menu()
