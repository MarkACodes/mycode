#!/usr/bin/env python3


from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['API_KEY'] = '9292929128049asdasd'

posts = [
    {
        'author': 'Bill Nye ',
        'title': 'Not Just a Science Guy - Post 1',
        'content': 'First post ',
        'date_posted': 'January 1, 2019'
    },
    {
        'author': 'Joanna Jones',
        'title': 'Blog Post 2',
        'content': 'Adventures in Australia - Second post ',
        'date_posted': 'February 1, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/login2", methods=['GET', 'POST'])
def login1():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'someone@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Did not work. Please check user login and your password', 'danger mr. robinson')
            return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)



