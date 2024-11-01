# python-cli-project
Budget Tracker CLI Application
Project Overview
The Budget Tracker is a command-line interface (CLI) application that helps users manage their finances by tracking budgets and expenses. With this application, users can create multiple budgets, add expenses under each budget, and easily view or delete their financial data. The application leverages SQLAlchemy ORM and SQLite for robust data management and persistence.

Table of Contents
Features
Project Structure
Setup and Installation
Usage
Example Workflow
Technologies Used
Features
User Management: Create, view, and delete users.
Budget Management: Create multiple budgets for each user, such as “Food,” “Transport,” or “Entertainment,” and set spending limits.
Expense Tracking: Track individual expenses under each budget.
Detailed User View: View all user details, including budgets and expenses.
Project Structure
plaintext

budget_tracker/
│
├── models/
│   ├── __init__.py           # Initializes models as a module
│   ├── database.py           # Sets up SQLite database and session
│   ├── user.py               # Defines User model and user-related methods
│   ├── budget.py             # Defines Budget model and budget-related methods
│   └── expense.py            # Defines Expense model and expense-related methods
│
├── cli.py                    # Main CLI interface with menu options
├── Pipfile                   # Dependency manager with required packages
├── README.md                 # Project documentation
└── .env                      # Environment file for database configurations (if needed)
Explanation of Each File
cli.py: The central command-line interface for the user to interact with the application. Contains options for managing users, budgets, and expenses.
models/database.py: Sets up the SQLite database using SQLAlchemy and provides the session management needed for all models.
models/user.py: Defines the User model and methods for user-related actions (e.g., creating, viewing, and deleting users).
models/budget.py: Defines the Budget model and methods to manage user budgets.
models/expense.py: Defines the Expense model and functions for tracking expenses.
Setup and Installation
Clone the Repository:

git clone https://github.com/your-username/budget-tracker.git
cd budget-tracker
Install Dependencies: Ensure you have Pipenv installed.

pipenv install
Activate the Virtual Environment:

pipenv shell
Run Migrations (if necessary): This ensures the database structure is created before use.

python models/database.py
Usage
To start the Budget Tracker application, run:

python cli.py
Main Menu Options
The CLI offers the following options:

Add User - Creates a new user with name and email.
View All Users - Displays a list of all users.
Add Budget - Creates a new budget under a specific user.
Add Expense - Adds an expense under a selected budget.
View User Details - Shows all budgets and expenses for a user.
Delete User - Deletes a user and associated data.
Exit - Closes the application.
Example Workflow
Add a User
Create a user with name and email.

Create a Budget for the User
Choose a budget category (e.g., "Food") and set a spending limit.

Add Expenses under the Budget
Add individual expenses (e.g., $20 for groceries).

View User Details
See all budgets and expenses for a selected user, including details for each entry.

Delete User
Remove a user and all associated budgets and expenses from the database.

Technologies Used
Python 3.8+
SQLAlchemy for ORM and database management
SQLite as the database
Pipenv for virtual environment and dependency management
Additional Notes
Make sure the .env file (if applicable) is configured correctly for database settings.
Run pipenv install each time a dependency is added or updated.
Happy tracking! 🎉