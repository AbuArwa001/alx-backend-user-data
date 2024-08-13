# 0x03. User Authentication Service

This project implements a user authentication service using Flask and SQLAlchemy. The goal is to understand the mechanisms behind user authentication by implementing it step-by-step.

## Learning Objectives

By the end of this project, you should be able to explain:
- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Requirements

- Python 3.7 on Ubuntu 18.04 LTS
- Code style: `pycodestyle` version 2.5
- SQLAlchemy 1.3.x
- bcrypt for password hashing: `pip3 install bcrypt`
- Flask for web framework: `pip3 install Flask`

## Project Structure

This project contains the following main components:

1. **User Model**
    - SQLAlchemy model named `User` for a database table named `users`.
    - Attributes: `id`, `email`, `hashed_password`, `session_id`, `reset_token`.
    - Example usage:
    ```python
    from user import User
    print(User.__tablename__)
    for column in User.__table__.columns:
        print("{}: {}".format(column, column.type))
    ```

2. **DB Class**
    - Manages the database connection and user operations.
    - Methods: `add_user`, `find_user_by`, `update_user`.
    - Example `add_user` method:
    ```python
    from db import DB
    my_db = DB()
    user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
    print(user_1.id)
    ```

3. **Auth Class**
    - Manages user authentication.
    - Methods: `register_user`, `valid_login`, `create_session`.
    - Example `register_user` method:
    ```python
    from auth import Auth
    email = 'me@me.com'
    password = 'mySecuredPwd'
    auth = Auth()
    user = auth.register_user(email, password)
    print("successfully created a new user!")
    ```

4. **Flask Application**
    - A basic Flask app with routes for user registration and session management.
    - Example route:
    ```python
    from flask import Flask, jsonify

    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def index():
        return jsonify({"message": "Bienvenue"})

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port="5000")
    ```

5. **Password Hashing**
    - Uses bcrypt to hash passwords.
    - Example `_hash_password` method:
    ```python
    from auth import _hash_password
    print(_hash_password("Hello Holberton"))
    ```

6. **Session Management**
    - Generate and store session IDs for users.
    - Example `create_session` method:
    ```python
    from auth import Auth
    email = 'bob@bob.com'
    password = 'MyPwdOfBob'
    auth = Auth()
    auth.register_user(email, password)
    print(auth.create_session(email))
    ```

## Usage

1. **Setting Up the Environment:**
    - Install the required packages:
    ```bash
    pip3 install -r requirements.txt
    ```

2. **Running the Application:**
    - Start the Flask server:
    ```bash
    python3 app.py
    ```

3. **Registering a User:**
    - Example POST request to register a user:
    ```bash
    curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd'
    ```

4. **Logging In:**
    - Example POST request to log in:
    ```bash
    curl -XPOST localhost:5000/sessions -d 'email=bob@me.com' -d 'password=mySuperPwd'
    ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
