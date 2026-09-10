# ExpenseTracker

#### Video Demo: https://youtu.be/94cA2KIAFA4

#### Description:

ExpenseTracker is a web application designed to help users keep track of their income and expenses in one simple place. I created this project as my CS50x Final Project because managing personal money is a practical problem that many people face. Instead of writing expenses down manually or trying to remember them, a user can use ExpenseTracker to record transactions and quickly see their financial summary.

The application starts with a registration and login system. A new user can create an account by providing a username and password. Passwords are not stored as plain text. Instead, the application uses password hashing before saving them to the database. Once a user logs in, a Flask session keeps track of the logged-in user so that the application can show that user's transactions.

The main page is the center of the application. It displays a welcome message and provides navigation links to the main features. The user can add an expense, add income, or log out. The page also displays a money summary containing total income, total expenses, and the current balance. The current balance is calculated by subtracting the total expenses from the total income. This gives the user a quick way to understand their current financial situation.

Users can add expenses by going to the Add Expense page. The form asks for a description, an amount, and a category. The available categories include Food, Transport, School, Shopping, and Other. The application checks that all required fields have been provided and that the amount is greater than zero before saving the transaction. Expenses are stored in the database with their type set to `expense`.

Users can also add income through the Add Income page. The user provides a description and an amount. The application performs similar validation before saving the transaction. Income is stored with its type set to `income`. Both income and expenses are displayed together in the transaction list on the homepage. Each transaction shows its type, description, amount, category, and creation date and time.

Another feature is the ability to delete transactions. Every transaction has its own database ID. When the user clicks the Delete button, the application sends a request containing that transaction ID. The Flask application then deletes the transaction only when it belongs to the currently logged-in user. This prevents a user from deleting another user's transaction.

The project is built using Python, Flask, SQLite, HTML, and CSS. Python is used for the main application logic, while Flask handles the web routes and requests. SQLite was chosen as the database because it is lightweight, simple to use, and appropriate for a small application like ExpenseTracker. I did not use a larger database system because the project does not require the complexity of a server-based database. SQLite also makes the project easier to run and understand.

The main Python file is `app.py`. This file contains the Flask application and the routes that control the application. It creates the Flask app, connects to the SQLite database, manages user registration and login, creates sessions, adds expenses, adds income, calculates totals, and deletes transactions. The `/` route loads the user's transactions and calculates total income, total expenses, and balance. The `/register` route handles account creation, while `/login` and `/logout` handle authentication. The `/add` route handles expenses, the `/income` route handles income, and the `/delete/<int:transaction_id>` route handles deleting transactions.

The `expenses.db` file is the SQLite database used by the application. It contains two main tables: `users` and `transactions`. The `users` table stores each user's ID, username, and password hash. The `transactions` table stores the transaction ID, user ID, transaction type, category, description, amount, and creation date. The `user_id` field connects transactions to the user who created them.

The `templates` folder contains the HTML pages used by Flask. `index.html` is the main homepage and displays the user's financial summary and transactions. `login.html` contains the login form. `register.html` contains the registration form. `add.html` contains the form for adding expenses. `income.html` contains the form for adding income. I kept these pages separate because each page has a specific purpose, which makes the project easier to understand and maintain.

The `static` folder contains `styles.css`. This file controls the appearance of the application, including the page layout, fonts, buttons, links, form inputs, and background. I decided to keep the design simple rather than adding a complicated frontend framework. This keeps the project focused on its main purpose while still making the application more pleasant to use.

One important design decision was to store both income and expenses in the same `transactions` table instead of creating separate tables. The `type` column identifies whether a transaction is income or an expense. I chose this approach because both types of transactions contain similar information, such as an amount, description, date, and user ID. Keeping them together makes it easier to display a complete transaction history and calculate totals using SQL queries.

Another design decision was to require users to log in before adding or viewing their transactions. This means that each user's financial information is connected to their own account. When querying or deleting transactions, the application uses the logged-in user's ID so that transactions remain associated with the correct account.

I also chose to keep the application intentionally simple. Instead of adding many unnecessary features, I focused on the core functions that make the application useful: authentication, adding income, adding expenses, viewing transactions, calculating a balance, and deleting transactions. This allowed me to build a complete application while keeping the code understandable.

ExpenseTracker demonstrates how Python, Flask, SQL, HTML, and CSS can work together to create a functional web application. The project also gave me experience with databases, user authentication, sessions, forms, SQL queries, validation, and connecting a frontend to backend logic.

AI assistance: ChatGPT was used to help explain programming concepts, troubleshoot errors, debug parts of the application, and assist with developing some of the code. I reviewed and tested the code while building the project.
