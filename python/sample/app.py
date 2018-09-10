from flask import Flask
from blueprint import tree_mold

app = Flask(__name__)


app.register_blueprint(tree_mold)
app.register_blueprint(tree_mold, url_prefix='/apple')
app.register_blueprint(tree_mold, url_prefix='/orange')