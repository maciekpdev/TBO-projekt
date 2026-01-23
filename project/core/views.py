from flask import render_template, Blueprint
import urllib3 


# Blueprint for core
core = Blueprint('core', __name__, template_folder='templates', static_folder='static')


# Route to homepage
@core.route('/')
def index():
    print('Homepage accessed')
    http = urllib3.PoolManager()
    return render_template('index.html')
