from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'super secret key'
Bootstrap(app)
from inventory_manager.app.routes import routes

