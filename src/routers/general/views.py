from flask import render_template

from . import general_api


@general_api.route('/', methods=['GET'])
def home():
    return render_template('index.html')
