from flask import Flask
from .routes import routes
import os

def create_app():
    # Absolute path to the project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    # Explicit template folder
    template_dir = os.path.join(project_root, "templates")

    app = Flask(
        __name__,
        template_folder=template_dir,
        static_folder=os.path.join(project_root, "static")
    )

    app.register_blueprint(routes)
    return app