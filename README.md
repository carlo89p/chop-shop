# Chop Shop API

A REST API for a mechanic shop built with Flask and MySQL. Handles customers, mechanics, and service tickets.

## Tech

- Flask
- SQLAlchemy
- Marshmallow
- MySQL
- python-dotenv

## Setup

1. Create and activate a virtual environment: python -m venv venv then venv\Scripts\activate
2. Install dependencies: pip install -r requirements.txt
3. Create a .env file in the root: SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://root:yourpassword@localhost/chop_shop
4. Create the chop_shop database in MySQL
5. Run it

## Status Codes

200 - OK, request worked
201 - Created, new record was added
400 - Bad request, something wrong with the data you sent. Check your JSON for missing fields or typos
404 - Not found, the id you used doesnt exist in the database
405 - Method not allowed, that route doesnt support that HTTP method
500 - Server error, something broke on the backend
