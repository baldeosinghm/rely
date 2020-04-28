# Rely
[Rely](http://45.56.102.63/ "Rely's Homepage"): A web app you can rely on to forecast today's stock market.

## Introduction?

Rely is a Flask web application that implements four machine learning algorithm
to predict stock prices. Namely, those stocks are Twitter, Verizon, Facebook,
Tesla, and Google. You can forecast up to five days in the future using the below
machine learning algorithms:

- Linear Regression Algorithm
- K Fold Cross-Validation Algorithm
- Support Vector Regression Algorithm
- Naive Bayes Classification Algorithm

You can access the app here: http://45.56.102.63/

## Usage Instructions

Rely is an open source project.  If you are a interested in using the software
for your own development, clone it from above with HTTPS or paste below into your
terminal:

```
git clone https://github.com/baldeosinghm/rely.git
```

### Install Dependencies

Rely is only operational when certain dependencies are installed.  It is highly
recommended that you to create a virtual environment before any change to code.
Once inside the Rely repository, install `pipenv`, a dependency manager for Python projects.

Use pip to install pipenv:
```
pip install --user pipenv
```

Navigate to the directory `rely/flaskapp/` and start virtual environment:
```
pipenv shell
```

Install app dependencies:

```
pipenv install --dev
```

### Run Application

Navigate to the inside of the /flaskapp directory and run:

```
python relyApp.py
```

Paste **localhost:5000** into browser to run application.
