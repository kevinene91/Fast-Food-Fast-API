from flask import redirect 
import os 
from app import create_app
"""
    app run point
"""
config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)


@app.route('/')
def home():
    return redirect('https://fastfoodfast1.docs.apiary.io/#reference/auth/auth-signup')


if __name__ == '__main__':
    app.run()