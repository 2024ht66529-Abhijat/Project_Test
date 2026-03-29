from flask import Blueprint, jsonify, render_template
from .services import calculate_calories

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return render_template("index.html")

@routes.route("/calories/<int:weight>/<program>")
def get_calories(weight, program):
    try:
        calories = calculate_calories(weight, program)
        return jsonify({
            "weight": weight,
            "program": program.upper(),
            "calories": calories
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400