# Secure_Login_System

## Overview

The Secure Login System is a web-based authentication application developed using Python, Flask, SQLite, and bcrypt. The project demonstrates secure user registration and login functionality with password hashing, session management, and protection against common security threats such as SQL injection.

## Features

* User Registration
* User Login Authentication
* Password Hashing using bcrypt
* Secure Password Storage
* Session Management
* Logout Functionality
* Input Validation
* SQL Injection Protection using Parameterized Queries

## Technologies Used

* Python
* Flask
* SQLite
* bcrypt
* HTML

## Project Structure

Secure-Login-System/
│
├── app.py
├── users.db
├── templates/
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
├── requirements.txt
└── README.md

## How It Works

### User Registration

* Users create an account using a username and password.
* Passwords are hashed using bcrypt before being stored in the database.

### User Login

* User credentials are verified against stored records.
* bcrypt is used to compare the entered password with the stored hash.

### Session Management

* A session is created after successful login.
* Only authenticated users can access protected pages.

### Logout

* User sessions are destroyed upon logout.
* The user is redirected to the login page.

## Security Features

* Password Hashing with bcrypt
* SQL Injection Protection
* Input Validation
* Secure Session Handling

## Learning Outcomes

* Understanding Authentication Systems
* Password Hashing and Verification
* Web Application Security Basics
* Database Integration with Flask
* Session Management

## Installation

Install the required libraries:
pip install flask bcrypt

Run the application:
python app.py

Open in your browser:
https://secure-login-system-32tp.onrender.com

## Future Enhancements

* Two-Factor Authentication (2FA)
* Password Strength Validation
* Email Verification
* Password Reset Functionality

## Disclaimer

This project is developed for educational and learning purposes only.

## Author

Manepalli Neha Gandhi

Cyber Security Internship Project
