# **Budget Tracker CLI Application**

## **Project Overview**
The Budget Tracker is a command-line interface (CLI) application designed to help users manage their finances by tracking budgets and expenses. This application allows users to create multiple budgets, add expenses under each budget, and view or delete financial data easily. It leverages SQLAlchemy ORM and SQLite for efficient data management and persistence.

---

## **Table of Contents**
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Setup and Installation](#setup-and-installation)
4. [Usage](#usage)
5. [Example Workflow](#example-workflow)
6. [Technologies Used](#technologies-used)
7. [Additional Notes](#additional-notes)

---

## **Features**
- **User Management:** Create, view, and delete users.
- **Budget Management:** Create multiple budgets per user, such as "Food," "Transport," or "Entertainment," with spending limits.
- **Expense Tracking:** Record individual expenses under each budget.
- **Detailed User View:** View comprehensive details for each user, including budgets and expenses.

---

## **Project Structure**

```plaintext
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
```

---

## **Explanation of Each File**

- **`cli.py`**: Main command-line interface where users interact with the application. Provides options for managing users, budgets, and expenses.
- **`models/database.py`**: Configures the SQLite database using SQLAlchemy and manages session creation for all models.
- **`models/user.py`**: Defines the User model and includes methods for user-related actions (e.g., creating, viewing, and deleting users).
- **`models/budget.py`**: Defines the Budget model and methods for managing user budgets.
- **`models/expense.py`**: Defines the Expense model and methods for tracking expenses.

---

## **Setup and Installation**

1. **Clone the Repository**:
    ```bash
    git clone git@github.com:Chege2004/python-cli-project.gitt
    cd python-cli-project
    ```

2. **Install Dependencies**:
   Ensure you have Pipenv installed, then run:
    ```bash
    pipenv install
    ```

3. **Activate the Virtual Environment**:
    ```bash
    pipenv shell
    ```

4. **Run Migrations** (if necessary):
   This creates the database structure.
    ```bash
    python models/database.py
    ```

---

## **Usage**

To start the Budget Tracker application, run:
```bash
python cli.py
```

### **Main Menu Options**
The CLI provides the following options for managing budgets and expenses:
1. **Add User** - Creates a new user with name and email.
2. **View All Users** - Displays a list of all users.
3. **Add Budget** - Creates a new budget for a user, specifying category and spending limit.
4. **Add Expense** - Adds an expense under a selected budget.
5. **View User Details** - Shows all budgets and expenses for a specific user.
6. **Delete User** - Deletes a user and all associated data.
7. **Exit** - Exits the application.

---

## **Example Workflow**

1. **Add a User**: Create a user by entering a name and email.
2. **Create a Budget for the User**: Choose a budget category (e.g., "Food") and set a spending limit.
3. **Add Expenses under the Budget**: Record individual expenses, such as $20 for groceries.
4. **View User Details**: Display all budgets and expenses for a specific user, showing details for each entry.
5. **Delete User**: Remove a user along with all associated budgets and expenses from the database.

---

## **Technologies Used**
- **Python 3.8+**
- **SQLAlchemy** for ORM and database management
- **SQLite** as the database
- **Pipenv** for virtual environment and dependency management

---

## **Additional Notes**
- Ensure that the `.env` file (if applicable) is configured correctly for database settings.
- Run `pipenv install` each time you add or update a dependency.

---

## **Video Demonstration**

[Watch the Budget Tracker Demonstration](https://drive.google.com/file/d/1pKOnWrEGg2oFlZMej5qr65LEjNbqC78T/view?usp=sharing)

---

### Happy Tracking! 🎉
