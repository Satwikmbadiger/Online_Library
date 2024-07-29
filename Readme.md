<h1>Online Library Management System</h1>

<h2>Overview</h2>
The Online Library Management System is a web application built using Django and Django-Ninja that allows users to manage books in a library, including borrowing and returning them. The system supports different user roles, including superusers/admin, and regular-users, each with different levels of access and functionality.

<h2>YouTube Link:</h2>https://youtu.be/RuijVNFu77s

<h2>Features</h2>

<h3>User Management:</h3>
Signup and signin functionality.
Profile management, including updating and deleting accounts.
User roles: Superuser/Admin and Regular-users.

<h3>Book Management:</h3>
Admin functionalities for adding, updating, deleting, and viewing books.
Users can view available books, borrow them, and return them.
Track borrowed books and their status.

<h3>Error Handling:</h3>
Unified error handling with user-friendly messages.
<br>
<h2>Installation</h2>

<h3>Prerequisites</h3>
Python 3.x
Django
Django-Ninja


<h3>Setup</h3>
<h3>Clone the repository:

<h3>bash</h3>
Copy code
git clone https://github.com/yourusername/your-repository.git
cd your-repository
Create a virtual environment:

<h3>bash</h3>
Copy code
python -m venv venv
Activate the virtual environment:

<h3>On Windows:</h3>

<h3>bash</h3>
Copy code
venv\Scripts\activate
On macOS/Linux:

<h3>bash</h3>
Copy code
source venv/bin/activate
Install dependencies:

<h3>bash</h3>
Copy code
pip install -r requirements.txt
Apply migrations:

<h3>bash</h3>
Copy code
python manage.py migrate
Create a superuser (if necessary):

<h3>bash</h3>
Copy code
python manage.py createsuperuser
Run the development server:

<h3>bash</h3>
Copy code
python manage.py runserver
Access the application:

Open your web browser and navigate to http://127.0.0.1:8000/.</h3>

<h2>Usage</h2>

<h3>The Online Library Management System supports the following functionalities:</h3>
<h3>Signup:</h3> Register a new account through the signup page.
<h3>Signin:</h3> Log in using your credentials.
<h3>Profile:</h3> Manage your profile, update details, or delete your account.
<h3>Books:</h3> Admin users can manage books, while regular users can view, borrow, and return books.
<h3>Error Handling:</h3> All errors are handled gracefully with user-friendly messages.
<h3>Dashboard:</h3> View the dashboard with relevant information based on your user role.

<h2>File Structure</h2>

Check the directory structure for refernce...

<h2>Contributing</h2>

<h3>Contributions are welcome! Here's how you can contribute to this project-</h3>
Fork the repository.<br>
Create a new branch (git checkout -b feature-branch).<br>
Make your changes.<br>
Commit your changes (git commit -am 'Add new feature').<br>
Push to the branch (git push origin feature-branch).<br>
Create a pull request.<br>

<h2>License</h2>
This project is open source and licensed using MT Licence.

<h2>Contact</h2>
For any inquiries or issues, please contact satwikmbadiger@gmail.com.
