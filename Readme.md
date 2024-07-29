Online Library Management System

Overview
The Online Library Management System is a web application built using Django and Django-Ninja that allows users to manage books in a library, including borrowing and returning them. The system supports different user roles, including superusers/admin, and regular-users, each with different levels of access and functionality.

Features

User Management:
Signup and signin functionality.
Profile management, including updating and deleting accounts.
User roles: Superuser/Admin and Regular-users.

Book Management:
Admin functionalities for adding, updating, deleting, and viewing books.
Users can view available books, borrow them, and return them.
Track borrowed books and their status.

Error Handling:
Unified error handling with user-friendly messages.


Installation

Prerequisites
Python 3.x
Django
Django-Ninja


Setup
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/your-repository.git
cd your-repository
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser (if necessary):

bash
Copy code
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the application:

Open your web browser and navigate to http://127.0.0.1:8000/.

Usage

The Online Library Management System supports the following functionalities:
Signup: Register a new account through the signup page.
Signin: Log in using your credentials.
Profile: Manage your profile, update details, or delete your account.
Books: Admin users can manage books, while regular users can view, borrow, and return books.
Error Handling: All errors are handled gracefully with user-friendly messages.
Dashboard: View the dashboard with relevant information based on your user role.

File Structure

Check the directory structure for refernce...

Contributing

Contributions are welcome! Here's how you can contribute to this project-
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a pull request.

License
This project is open source.

Contact
For any inquiries or issues, please contact satwikmbadiger@gmail.com.
