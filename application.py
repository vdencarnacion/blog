from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator

app = Flask(__name__)
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
