# Streamlit App with Authentication

This simple Streamlit app demonstrates user authentication using the streamlit-authenticator library.

## Features

    Requires users to log in with a username and password.
    Displays a short text block upon successful login.
    Includes a logout button.
    Hides some Streamlit elements for a cleaner interface.

## Setup

    Install the required libraries:
    Bash

    pip install streamlit streamlit-authenticator yaml

    Use code with caution.

Create a configuration file named config.yaml with the following structure:
YAML

credentials:
  usernames: ['user1', 'user2']  # Replace with your desired usernames
  hashed_passwords: ['hashed_password1', 'hashed_password2']  # Replace with hashed passwords
cookie:
  name: 'your_cookie_name'  # Choose a name for the authentication cookie
  key: 'your_secret_key'  # Generate a strong secret key
  expiry_days: 30  # Set the cookie expiration time

Use code with caution.

        Use the Hasher module from streamlit-authenticator to generate hashed passwords.

## Running the App

    Execute the Streamlit app:
    Bash

    streamlit run app.py

    Use code with caution.

## Additional Notes

    This project is intended for learning purposes; it may not follow all best practices for production-grade authentication.
    Consider exploring more advanced features of the streamlit-authenticator library for additional functionality.
