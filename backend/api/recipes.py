# /backend/api/recipes.py

from flask import Blueprint, request, jsonify

# Create a blueprint for the recipes API
recipes_bp = Blueprint('recipes', __name__, url_prefix='/api/recipes')

# Endpoint to get all recipes
@recipes_bp.route("/", methods=["GET"])
def get_recipes():
    try:
        
        # Convert recipes to a list of dictionaries
        recipes_list = [{
            "id": 123,
            "title": 'Spaghetti',
            "ingredients": 'Stuff',
            "instructions": 'do this'
        }]
        
        # Return the list of recipes as JSON
        return jsonify(recipes_list), 200
    except Exception as e:
        return jsonify({"message": "Failed to fetch recipes", "error": str(e)}), 500

