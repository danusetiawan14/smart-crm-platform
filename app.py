from flask import Flask

from config import Config
from extensions import db

from routes.main import main


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

# Register Blueprint
app.register_blueprint(main)


if __name__ == "__main__":
    app.run(debug=True)