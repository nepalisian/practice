from flask import Flask
from app import tree_mold

application = Flask(__name__)
application.register_blueprint(tree_mold, url_prefix='/oak')
application.register_blueprint(tree_mold, url_prefix='/apple')

