# HouseHunt
This is the Flask module Group project for Moringa Core.

## Description

A website where real estate agents looking to market their houses can display them and users looking to rent or buy houses can book appointments to view the houses on display

## Features/User Stories
- The website allows users to view various listings based on categories.
- An agent can upload a listing
- An agent caan set time appointments for users to view listed listings
- Agents can create accounts and sign in for them to list houses.
- Users can book appointments to view listings

## Behavior Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View all listings based on various \categories | Default Home Page <br> Click on a category to see listings | Displays all listingss |
| Register as a user | Click `register` on the navbar | Redirects to registration page to sign up |
| Log in as a user | Click on `log in` | Redirects to log in page |
| Update your Profile | Click on `Profile` | Redirects to profile page where you can update your bio and profile picture |
| Upload a listing | Click on `Upload listing`on the navbar | Redirects to listings form page where you may create a new listing|
| Book appointment to view Listing | Click on `Book View` button when logged in | Creates a new booking appointment  |


## View Live Site here
View the complete site [here](https://househunt-group.herokuapp.com/)


## Technologies Used
    - Python 3.6
    - Flask Framework
    - HTML, CSS and Bootstrap
    - JavaScript
    - Postgressql
    - Heroku


## Set-up and Installation
    1. Clone or download the Repo
    2. Create a virtual environment:
        sudo apt-get install python3.6-venv
        python3.6 -m venv virtual source virtual/bin/activate
    3. Read the specs and requirements files and Install all the requirements.
    4. Install dependancies that will create an environment for the app to run:
        pip3 install -r requirements
    5. Edit the start.sh file to prepare your environment variables:
        export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchit'
        export SECRET_KEY='Your secret key'
        export MAIL_USERNAME='Your email'
        export MAIL_PASSWORD='Your email password'
    6. Run database migrations:
        python manage.py db init
        python manage.py db migrate -m "initial migration"
        python manage.py db upgrade
    7. Run chmod a+x start.py
    8. Run ./start.py
    9. Access the application through `localhost:5000`

### Contributions
Yet to complete all tests for each model class. If you have ideas you may contribute to this project.

## Known bugs
No known bugs so far. If found drop me an email.


## Contributors
    - Sophia Murage
    - Clifford Kasera
    - Wanjiru Nganga
    - Adiela Abishua

