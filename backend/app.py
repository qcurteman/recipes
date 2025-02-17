from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Import the Recipe model and register the blueprint
from api.recipes import recipes_bp
app.register_blueprint(recipes_bp)

# Enable CORS for all routes
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
