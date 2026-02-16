from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.after_request
def log_response(response):
    print(f"{request.method} {request.path} → Status: {response.status_code}")
    return response

FILES = {
    "restaurants": "restaurants.json",
    "dishes": "dishes.json",
    "users": "users.json",
    "orders": "orders.json",
    "ratings": "ratings.json"
}

# ==============================
# HELPERS
# ==============================

def read_data(key):
    if not os.path.exists(FILES[key]):
        return []
    with open(FILES[key], "r") as f:
        return json.load(f)

def write_data(key, data):
    with open(FILES[key], "w") as f:
        json.dump(data, f, indent=4)

def generate_id(data):
    return len(data) + 1

# ==============================
# RESTAURANTS
# ==============================

@app.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    required_fields = ["name", "category", "location", "images", "contact"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field.capitalize()} required"}), 400

    restaurants = read_data("restaurants")

    if any(r["name"] == data["name"] for r in restaurants):
        return jsonify({"error": "Restaurant exists"}), 409

    restaurant = {
        "id": generate_id(restaurants),
        "name": data["name"],
        "category": data["category"],
        "location": data["location"],
        "images": data["images"],
        "contact": data["contact"],
        "approved": False,
        "active": True
    }

    restaurants.append(restaurant)
    write_data("restaurants", restaurants)

    return jsonify(restaurant), 201


@app.route("/api/v1/restaurants", methods=["GET"])
def list_restaurants():
    return jsonify(read_data("restaurants")), 200


@app.route("/api/v1/restaurants/<int:rid>", methods=["GET"])
def view_restaurant(rid):

    restaurants = read_data("restaurants")
    restaurant = next((r for r in restaurants if r["id"] == rid), None)

    if not restaurant:
        return jsonify({"error": "Not found"}), 404

    return jsonify(restaurant), 200


# ✅ UPDATE RESTAURANT (Fix for 405)
@app.route("/api/v1/restaurants/<int:rid>", methods=["PUT"])
def update_restaurant(rid):

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    restaurants = read_data("restaurants")
    restaurant = next((r for r in restaurants if r["id"] == rid), None)

    if not restaurant:
        return jsonify({"error": "Not found"}), 404

    for field in ["name", "category", "location", "images", "contact", "active"]:
        if field in data:
            restaurant[field] = data[field]

    write_data("restaurants", restaurants)

    return jsonify(restaurant), 200


@app.route("/api/v1/restaurants/search", methods=["GET"])
def search_restaurants():

    name = request.args.get("name", "").lower()
    location = request.args.get("location", "").lower()

    restaurants = read_data("restaurants")

    filtered = [
        r for r in restaurants
        if name in r["name"].lower()
        and location in r["location"].lower()
    ]

    return jsonify(filtered), 200

# ==============================
# DISHES
# ==============================

@app.route("/api/v1/restaurants/<int:rid>/dishes", methods=["POST"])
def add_dish(rid):

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON body required"}), 400

    required_fields = ["name", "type", "price", "available_time", "image"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field.replace('_',' ').capitalize()} required"}), 400

    dishes = read_data("dishes")

    dish = {
        "id": generate_id(dishes),
        "restaurant_id": rid,
        "name": data["name"],
        "type": data["type"],
        "price": data["price"],
        "available_time": data["available_time"],
        "image": data["image"],
        "enabled": True
    }

    dishes.append(dish)
    write_data("dishes", dishes)

    return jsonify(dish), 201


@app.route("/api/v1/dishes/<int:did>", methods=["PUT"])
def update_dish(did):

    data = request.get_json()

    dishes = read_data("dishes")
    dish = next((d for d in dishes if d["id"] == did), None)

    if not dish:
        return jsonify({"error": "Not found"}), 404

    for field in ["name", "type", "price", "available_time", "image"]:
        if field in data:
            dish[field] = data[field]

    write_data("dishes", dishes)

    return jsonify(dish), 200


@app.route("/api/v1/dishes/<int:did>/status", methods=["PUT"])
def update_dish_status(did):

    data = request.get_json()

    if not data or "enabled" not in data:
        return jsonify({"error": "Enabled flag required"}), 400

    dishes = read_data("dishes")
    dish = next((d for d in dishes if d["id"] == did), None)

    if not dish:
        return jsonify({"error": "Not found"}), 404

    dish["enabled"] = data["enabled"]
    write_data("dishes", dishes)

    return jsonify({"message": "Dish status updated"}), 200


@app.route("/api/v1/dishes/<int:did>", methods=["DELETE"])
def delete_dish(did):

    dishes = read_data("dishes")
    dish = next((d for d in dishes if d["id"] == did), None)

    if not dish:
        return jsonify({"error": "Not found"}), 404

    dishes.remove(dish)
    write_data("dishes", dishes)

    return jsonify({"message": "Dish deleted"}), 200

# ==============================
# USERS
# ==============================

@app.route("/api/v1/users/register", methods=["POST"])
def register_user():

    data = request.get_json()

    required_fields = ["name", "email", "password"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field.capitalize()} required"}), 400

    users = read_data("users")

    if any(u["email"] == data["email"] for u in users):
        return jsonify({"error": "User exists"}), 409

    user = {
        "id": generate_id(users),
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    }

    users.append(user)
    write_data("users", users)

    return jsonify(user), 201

# ==============================
# ORDERS
# ==============================

@app.route("/api/v1/orders", methods=["POST"])
def place_order():

    data = request.get_json()

    required_fields = ["user_id", "restaurant_id", "dishes"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field.capitalize()} required"}), 400

    orders = read_data("orders")

    order = {
        "id": generate_id(orders),
        "user_id": data["user_id"],
        "restaurant_id": data["restaurant_id"],
        "dishes": data["dishes"],
        "status": "Placed"
    }

    orders.append(order)
    write_data("orders", orders)

    return jsonify(order), 201


@app.route("/api/v1/restaurants/<int:rid>/orders", methods=["GET"])
def orders_by_restaurant(rid):

    orders = read_data("orders")
    filtered = [o for o in orders if o["restaurant_id"] == rid]

    return jsonify(filtered), 200


@app.route("/api/v1/users/<int:uid>/orders", methods=["GET"])
def orders_by_user(uid):

    orders = read_data("orders")
    filtered = [o for o in orders if o["user_id"] == uid]

    return jsonify(filtered), 200

# ==============================
# RATINGS
# ==============================

@app.route("/api/v1/ratings", methods=["POST"])
def give_rating():

    data = request.get_json()

    required_fields = ["order_id", "rating", "comment"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field.capitalize()} required"}), 400

    ratings = read_data("ratings")

    rating = {
        "id": generate_id(ratings),
        "order_id": data["order_id"],
        "rating": data["rating"],
        "comment": data["comment"]
    }

    ratings.append(rating)
    write_data("ratings", ratings)

    return jsonify(rating), 201

# ==============================
# ADMIN MODULE
# ==============================

@app.route("/api/v1/admin/restaurants/<int:rid>/approve", methods=["PUT"])
def approve_restaurant(rid):

    restaurants = read_data("restaurants")
    restaurant = next((r for r in restaurants if r["id"] == rid), None)

    if not restaurant:
        return jsonify({"error": "Not found"}), 404

    restaurant["approved"] = True
    write_data("restaurants", restaurants)

    return jsonify({"message": "Restaurant approved"}), 200


@app.route("/api/v1/admin/restaurants/<int:rid>/status", methods=["PUT"])
def update_restaurant_status(rid):

    data = request.get_json()

    if not data or "active" not in data:
        return jsonify({"error": "Active flag required"}), 400

    restaurants = read_data("restaurants")
    restaurant = next((r for r in restaurants if r["id"] == rid), None)

    if not restaurant:
        return jsonify({"error": "Not found"}), 404

    restaurant["active"] = data["active"]
    write_data("restaurants", restaurants)

    return jsonify({"message": "Restaurant status updated"}), 200



@app.route("/api/v1/admin/feedback", methods=["GET"])
def view_feedback():
    return jsonify(read_data("ratings")), 200


@app.route("/api/v1/admin/orders", methods=["GET"])
def view_all_orders():
    return jsonify(read_data("orders")), 200

# ==============================

if __name__ == "__main__":
    app.run(debug=True, port=5006)