from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

patients = []

@app.route("/")
def home():
    return render_template("patient.html", patients=patients)

@app.route("/register", methods=["POST"])
def register():
    data = request.form.to_dict()
    patients.append(data)
    return render_template("patient.html", patients=patients)

@app.route("/api/patients", methods=["GET", "POST"])
def patient_api():
    if request.method == "GET":
        return jsonify(patients)

    data = request.json
    if not data or not data.get("name"):
        return jsonify({"error": "Invalid data"}), 400

    patients.append(data)
    return jsonify({"message": "Patient added"}), 201

@app.route("/api/patients/<int:id>", methods=["GET", "PUT"])
def patient_by_id(id):
    try:
        if request.method == "GET":
            return jsonify(patients[id])

        patients[id].update(request.json)
        return jsonify({"message": "Patient updated"})
    except IndexError:
        return jsonify({"error": "Patient not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
