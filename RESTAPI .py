from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users (user_id as key)
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

# GET specific user by id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

# POST create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not "name" in data or not "email" in data:
        return jsonify({"error": "Invalid input"}), 400
    user_id = max(users.keys(), default=0) + 1
    user = {"id": user_id, "name": data["name"], "email": data["email"]}
    users[user_id] = user
    return jsonify(user), 201

# PUT update user details
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    users[user_id].update({k: v for k, v in data.items() if k in ["name", "email"]})
    return jsonify(users[user_id]), 200

# DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        deleted = users.pop(user_id)
        return jsonify({"message": "User deleted", "user": deleted}), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '_main_':
    app.run(debug=True)