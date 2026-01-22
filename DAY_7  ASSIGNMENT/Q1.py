from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
users = [
    {"id": 1, "name": "Balu", "email": "balu123@example.com"},
    {"id": 2, "name": "Ajay", "email": "ajay123@example.com"}
]


# Root route (optional but helpful)
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "User API is running"}), 200


# GET /users → Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# GET /users/<id> → Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200


# POST /users → Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(new_user)
    return jsonify(new_user), 201


# PUT /users/<id> → Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not data:
        return jsonify({"error": "No data provided"}), 400

    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])

    return jsonify(user), 200


# DELETE /users/<id> → Delete user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
