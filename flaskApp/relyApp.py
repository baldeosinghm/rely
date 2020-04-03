from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, PredictForm
from src.generate_csv import get_endpoint
import sys

app = Flask(__name__)
app.config["SECRET_KEY"] = "db42fc934f31476f881c17cef872296e"


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    form = PredictForm()
    if form.validate_on_submit():
        data=request.form["stockTicker"]
        get_endpoint(data)
    return render_template('predict.html', title='Predict', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

if __name__ == '__main__':
    app.run(debug=True)
