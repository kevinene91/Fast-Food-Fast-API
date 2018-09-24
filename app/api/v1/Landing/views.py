from flask import Blueprint, render_template


landing_page = Blueprint('landing', '___name__', template_folder='templates' )

@landing_page.route('/', methods=['GET', 'POST'])
def landing():
    return render_template('index.html')