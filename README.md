Tickets
Overview
"Tickets" is a comprehensive backend project developed to manage ticketing systems. This project is designed to demonstrate the use of various backend technologies and frameworks, including Python, Docker, PostgreSQL, and MongoDB.

Features
User Authentication: Secure user login and registration.

Ticket Management: Create, update, and delete tickets.

Database Integration: Efficient data handling using PostgreSQL and MongoDB.

API Integration: RESTful API implementation for seamless data exchange.

Dockerization: Containerized application for easy deployment and management.

Technologies Used
Programming Language: Python

Framework: Django

Databases: PostgreSQL, MongoDB

Containerization: Docker

Version Control: Git

Development Progress
Current Stage: Deployment

Next Steps: Optimize the frontend

Installation
Clone the repository:

bash
git clone https://github.com/NewtYao/Tickets.git
cd Tickets
Set up the virtual environment:

bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the dependencies:

bash
pip install -r requirements.txt
Set up the databases:

Ensure PostgreSQL and MongoDB are installed and running.

Create a PostgreSQL database and update the DATABASES settings in settings.py.

Run the migrations:

bash
python manage.py migrate
Start the development server:

bash
python manage.py runserver
Usage
Navigate to http://127.0.0.1:8000/ in your web browser.

Register a new user or log in with existing credentials.

Manage your tickets using the provided interfaces.

Contribution
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.
