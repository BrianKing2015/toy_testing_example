# toy_testing_example
A very simple web api example with tests.
This is meant as a simple example project against which to try different testing methods. The three methods that have already been created are:

- Realistic style data (faker library)
- Property based testing (Hypothesis)
- Load testing (Locust)


# Getting Started

- Create a virtual environment (venv, conda, etc.)
- Run pip install -r requirements.txt to install the required libraries 
- Open the database_creation.py file and run the create_db_table function
- Run the Flask app in app.py
- In the tests folder
  - test_faker.py has examples of each type of CRUD action as REST calls
    - Meant to be run from PyTest and should complete in less than 1 minute
    - Shows that the Flask app continues to perform basic tasks
  - test_property_based.py
    - Meant to be run from PyTest and can run for significantly longer
    - Explores what inputs are allowed by semi-randomly iterating through values
  - load_test_file.py
    - Meant to be run with Locust from the commandline
    - Allows generating load to see when/where things break
    - Example command in terminal: 'locust -f .\toy_example\tests\load_testing_file.py'
    - This will spawn a web interface at localhost:8089 that allows for control and metrics output
  