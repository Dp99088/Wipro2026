from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

MOVIES_FILE = "movies.json"
BOOKINGS_FILE = "bookings.json"


def read_json(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, "r") as file:
        return json.load(file)


def write_json(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


# ---------------- MOVIES API ----------------

@app.route("/api/movies", methods=["GET"])
def get_movies():
    movies = read_json(MOVIES_FILE)
    return jsonify(movies), 200


@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movies = read_json(MOVIES_FILE)
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/movies", methods=["POST"])
def add_movie():
    movies = read_json(MOVIES_FILE)
    data = request.json
    movies.append(data)
    write_json(MOVIES_FILE, movies)
    return jsonify(data), 201


@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    movies = read_json(MOVIES_FILE)
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(request.json)
            write_json(MOVIES_FILE, movies)
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    movies = read_json(MOVIES_FILE)
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            write_json(MOVIES_FILE, movies)
            return jsonify({"message": "Movie deleted"}), 200
    return jsonify({"error": "Movie not found"}), 404


# ---------------- BOOKINGS API ----------------

@app.route("/api/bookings", methods=["POST"])
def book_tickets():
    movies = read_json(MOVIES_FILE)
    bookings = read_json(BOOKINGS_FILE)

    data = request.json
    movie_id = data.get("movie_id")
    seats = data.get("seats")

    for movie in movies:
        if movie["id"] == movie_id:
            booking = {
                "movie_id": movie_id,
                "seats": seats,
                "total_price": seats * movie["price"]
            }
            bookings.append(booking)
            write_json(BOOKINGS_FILE, bookings)
            return jsonify(booking), 201

    return jsonify({"error": "Booking failed. Movie not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5001)
