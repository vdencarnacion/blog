import os

from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, View
# , Subgroup, Link, Text, Separator

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('TRACK_MODIFICATIONS')

db.init_app(app)

nav = Nav(app)

nav.register_element('my_navbar',
                     Navbar('thenav',
                            View('Resume', 'index'),
                            View('Gallery', 'gallery'),
                            View('Blog', 'blog'),
                            View('Contact', 'contact')))


@app.route('/')
def index():
    title = 'resume'
    body = 'resume'
    return render_template('base.html', title=title, body=body)


@app.route('/gallery')
def gallery():
    title = 'gallery'
    body = 'gallery'
    return render_template('base.html', title=title, body=body)


@app.route('/blog')
def blog():
    title = 'blog'
    body = 'blog'
    return render_template('base.html', title=title, body=body)


@app.route('/contact')
def contact():
    title = 'contact'
    body = 'contact'
    return render_template('base.html', title=title, body=body)


def main():
    db.create_all()


if __name__ == '__main__':
    with app.app_context():
        main()
