# flask_app/flask_app.py
"""
calculators.py - Powerlifting score calculators including McCullough
"""
import os
from flask import Flask, render_template, request, send_from_directory
from calculation.calculators import get_scores


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

    :return: render_template
    """
    scores = None
    if request.method == "POST":
        try:
            body_weight = float(request.form["body_weight"])
            total_lifted = float(request.form["total_lifted"])
            is_kg = request.form["unit"] == "kg"
            is_female = request.form["gender"] == "female"
            competition = request.form["competition"]
            scores = get_scores(
                body_weight,
                total_lifted,
                is_kg,
                is_female,
                competition
            )
        except ValueError:
            scores = None  # Handle invalid input
    return render_template("index.html", scores=scores)


if __name__ == "__main__":
    is_production = os.getenv("FLASK_ENV") == "production"

    # Explicitly bind to your local network IP (change IP if needed)
    app.run(host="192.168.0.246", port=5000, debug=not is_production)
