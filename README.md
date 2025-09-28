# RESTAPI
# Flask User Management API

A simple RESTful API built with **Flask** that supports basic **CRUD operations** for user management.  
This project uses in-memory storage (dictionary) for demonstration purposes.

---

## 🚀 Features
- Get all users (`GET /users`)
- Get a specific user by ID (`GET /users/<id>`)
- Create a new user (`POST /users`)
- Update an existing user (`PUT /users/<id>`)
- Delete a user (`DELETE /users/<id>`)

---

## 📦 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-user-api.git
   cd flask-user-api

2.Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


3.Install dependencies:
pip install flask

4.Run the server:
python app.py

The API will be available at:
👉 http://127.0.0.1:5000/
