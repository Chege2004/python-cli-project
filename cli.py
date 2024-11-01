from models.user import User
from models.budget import Budget
from models.expense import Expense

def user_menu():
    print("User Management:")
    print("1. Add User")
    print("2. View All Users")
    print("3. Create Budget for User")
    print("4. Add Expense to a Budget")
    print("5. View User Details")
    print("6. Delete User")  # New option for deleting a user
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
        user_id = int(input("Enter user ID to create budget for: "))
        category = input("Enter budget category: ")
        limit = float(input("Enter budget limit: "))
        Budget.create_budget(category, limit, user_id)
        print("Budget created successfully.")

    elif choice == "4":
        budget_id = int(input("Enter budget ID to add expense to: "))
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        Expense.create_expense(description, amount, budget_id)
        print("Expense added successfully.")

    elif choice == "5":
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

    elif choice == "6":  # New option to delete a user
        user_id = int(input("Enter user ID to delete: "))
        success = User.delete_user(user_id)
        if success:
            print("User deleted successfully.")
        else:
            print("User not found or could not be deleted.")

if __name__ == "__main__":
    user_menu()
