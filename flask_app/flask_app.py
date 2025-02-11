# flask_app/flask_app.py
"""
calculators.py - Powerlifting score calculators including McCullough
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template, request, send_from_directory, jsonify
from calculation.calculators import get_scores
import logging

logging.basicConfig(level=logging.DEBUG)

# Ensure Flask knows where to find templates and static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR
)


@app.route('/favicon.ico')
def favicon():
    """

    :return:
    """
    return send_from_directory(
        "static",
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon"
    )


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles form submission and calculates powerlifting scores.
    :return: Rendered HTML template with scores.
    """
    scores = None
    try:
        if request.method == "POST":
            body_weight = float(request.form["body_weight"])
            total_lifted = float(request.form["total_lifted"])
            is_kg = request.form["unit"] == "kg"
            is_female = request.form["gender"] == "female"
            competition = request.form["competition"]
            age = int(request.form["age"])
            scores = get_scores(
                body_weight,
                total_lifted,
                is_kg,
                is_female,
                competition,
                age
            )
    except ValueError as e:
        logging.error(f"Invalid input: {e}")
        scores = None
    return render_template("index.html", scores=scores)

app.config["LIFESPAN"] = False

@app.route("/api/v1/calculate", methods=["POST"])
def api_calculate():
    """
    API endpoint to return scores in JSON format.
    """
    try:
        data = request.json
        body_weight = float(data["body_weight"])
        total_lifted = float(data["total_lifted"])
        is_kg = data["unit"] == "kg"
        is_female = data["gender"] == "female"
        competition = data["competition"]
        age = int(data.get("age", 23))

        scores = get_scores(body_weight, total_lifted, is_kg, is_female, competition, age)
        return jsonify(scores)

    except (ValueError, KeyError) as e:
        logging.error(f"Invalid input: {e}")
        return jsonify({"error": "Invalid input"}), 400



if __name__ == "__main__":
    is_production = os.getenv("FLASK_ENV") == "production"
    app.run(host="192.168.0.246", port=5000, debug=not is_production)
