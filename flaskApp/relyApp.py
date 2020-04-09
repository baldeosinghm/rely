from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, PredictForm, PredictCvForm, PredictSvmForm
from src.generate_csv import stock_csv
from src.linear_regression import predictPrice
from src.crossValidation import cvPredictPrice
from src.support_vector_regression import vectorPredictPrice
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

@app.route("/linear", methods=['GET', 'POST'])
def linear():
    form = PredictForm()
    if form.validate_on_submit():
        stock=request.form["stockTicker"]
        days=int(request.form["daysToPredict"])
        stock_csv(stock)
        prediction=predictPrice(stock, days)
        if (days==1):
            flash("Linear Regression | " + str(stock) + "'s High in " + str(days) + " day will be: $" + str(prediction[0]) + ".")
        else:
            flash("Linear Regression | " + str(stock) + "'s High in " + str(days) + " days will be: $" + str(prediction[0]) + ".")
    return render_template('linear.html', title='Linear Regression', form=form)

@app.route("/kfold", methods=['GET', 'POST'])
def kfold():
    form = PredictCvForm()
    if form.validate_on_submit():
        stock=request.form["cVstockTicker"]
        days=int(request.form["cVdaysToPredict"])
        stock_csv(stock)
        predictionTwo=cvPredictPrice(stock, days)
        if (days==1):
            flash("K-Fold CV | " + str(stock) + "'s High in " + str(days) + " day will be: $" + str(predictionTwo[0]) + ".")
        else:
            flash("K-Fold CV | " + str(stock) + "'s High in " + str(days) + " days will be: $" + str(predictionTwo[0]) + ".")
    return render_template('kfold.html', title='K-Fold CV', form=form)

@app.route("/svm", methods=['GET', 'POST'])
def svm():
    form = PredictSvmForm()
    if form.validate_on_submit():
        stock=request.form["svMstockTicker"]
        days=int(request.form["svMdaysToPredict"])
        stock_csv(stock)
        predictionThree=vectorPredictPrice(stock, days)
        if (days==1):
            flash("Support Vector Machine | " + str(stock) + "'s High in " + str(days) + " day will be: $" + str(predictionThree) + ".")
        else:
            flash("Support Vector Machine | " + str(stock) + "'s High in " + str(days) + " days will be: $" + str(predictionThree) + ".")
    return render_template('svm.html', title='SVM', form=form)

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
