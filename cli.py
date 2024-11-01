from models.user import User
from models.budget import Budget
from models.expense import Expense

def user_menu():
    while True:
        print("\nUser Management:")
        print("1. Add User")
        print("2. View All Users")
        print("3. View User Details")
        print("4. Delete User")
        print("5. Return to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            User.create_user(name, email)
            print("User created successfully.")

        elif choice == "2":
            users = User.get_all_users()
            for user in users:
                print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

        elif choice == "3":
            user_id = int(input("Enter user ID to view details: "))
            user_details = User.get_user_details(user_id)
            if user_details:
                print(f"User ID: {user_id}")
                print(f"Name: {user_details['name']}")
                print(f"Email: {user_details['email']}")
                print("Budgets:")
                for budget in user_details['budgets']:
                    print(f"  - Category: {budget['category']}, Limit: {budget['limit']}")
                    print("    Expenses:")
                    for expense in budget['expenses']:
                        print(f"      * {expense['description']}: ${expense['amount']}")
            else:
                print("User not found.")

        elif choice == "4":
            user_id = int(input("Enter user ID to delete: "))
            User.delete_user(user_id)
            print("User deleted successfully.")

        elif choice == "5":
            break  # Exit to return to main menu

        else:
            print("Invalid option. Please try again.")

def budget_menu():
    while True:
        print("\nBudget Management:")
        print("1. Add Budget")
        print("2. View All Budgets")
        print("3. Return to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            user_id = int(input("Enter user ID for the budget: "))
            category = input("Enter budget category: ")
            limit = float(input("Enter budget limit: "))
            Budget.create_budget(category, limit, user_id)
            print("Budget created successfully.")

        elif choice == "2":
            budgets = Budget.get_all_budgets()
            for budget in budgets:
                print(f"ID: {budget.id}, Category: {budget.category}, Limit: {budget.limit}, User ID: {budget.user_id}")

        elif choice == "3":
            break  # Exit to return to main menu

        else:
            print("Invalid option. Please try again.")

def expense_menu():
    while True:
        print("\nExpense Management:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Return to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            budget_id = int(input("Enter budget ID for the expense: "))
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            Expense.create_expense(description, amount, budget_id)
            print("Expense created successfully.")

        elif choice == "2":
            expenses = Expense.get_all_expenses()
            for expense in expenses:
                print(f"ID: {expense.id}, Description: {expense.description}, Amount: {expense.amount}, Budget ID: {expense.budget_id}")

        elif choice == "3":
            break  # Exit to return to main menu

        else:
            print("Invalid option. Please try again.")

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. User Management")
        print("2. Budget Management")
        print("3. Expense Management")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            budget_menu()
        elif choice == "3":
            expense_menu()
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
