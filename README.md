------------------Running the Flask Application-------------
Prerequisites

    Python 3.x installed
    Flask installed (pip install Flask)
    ChromeDriver installed (for Selenium tests)

Steps to Run the Application

    Clone the Repository

    bash

git clone <repository-url>
cd <project-directory>

Set Up the Environment
Create and activate a virtual environment (optional but recommended):

bash

python3 -m venv venv
source venv/bin/activate

Install Dependencies
Install Flask and other required packages:

bash

pip install Flask

Create Environment Variables
Set the FLASK_APP environment variable to point to your application file:

bash

export FLASK_APP=app.py

Run the Flask Application
Start the Flask development server:

bash

    flask run

    The application will be available at http://127.0.0.1:5000.

Accessing the Application

    Login Page: http://127.0.0.1:5000/login
    Registration Page: http://127.0.0.1:5000/register

-----------------Running Automated Tests with Selenium--------------------
Prerequisites

    Python 3.x installed
    Selenium installed (pip install selenium)
    ChromeDriver installed and accessible in your system PATH

Steps to Run Tests

    Clone the Repository

    bash

git clone <repository-url>
cd <project-directory>/tests

Install Test Dependencies
Install Selenium if not already installed:

bash

pip install selenium

Run Tests
Execute the test scripts using Python:

bash

    python3 test_user_registration.py
    python3 test_user_login.py

Note

    Ensure the Flask application is running before executing tests.
    Update test URLs if the application is running on a different port.
