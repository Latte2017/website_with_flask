"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


post = [
    { 
        'author': 'Kiran',
        'title' : 'Blah',
        'content' : 'Another blah',
        'date_posted' : '1998'
    },
    { 
        'author': 'Teju',
        'title' : 'Blah2',
        'content' : 'Another blah2',
        'date_posted' : '1986'
    }
]


@app.route('/posts')
def posts():
    """ Renders the posts page"""
    return render_template(
        'posts.html', 
        post=post,
        title='Blog Posts',
        year=datetime.now().year,
        message='These are the blogs.'
        )
