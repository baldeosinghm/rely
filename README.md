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

This application has been deployed so it can be accessed here: http://45.56.102.63/

## Usage Instructions

Rely is an open source project.  If you are a interested in using the software
for your own development, clone it from above with HTTPS or paste below into your
terminal:

```
git clone https://github.com/baldeosinghm/rely.git
```

This tool uses Quandl's Time-Series API to retrieve historical stock prices.  Currently, my API token is being used.  However, you should replace it with one acquired via Quandl if you are to make any changes or avoid API call restrictions.  This can be done by navigating to the `generate_csv.py` module in the src folder and replacing the portion below entitled `API_token` with yours.

```
endpoint = requests.get("https://www.quandl.com/api/v3/datasets/WIKI/" + stock + "/data.json?api_key=API_token")
```

If you would like to manipulate a different dataset refer to Quandl's API documentation [here](https://docs.quandl.com).

### Install Dependencies

Rely is only operational when certain dependencies are installed.  It is highly
recommended that you create a virtual environment before any changes to the code
are made. Once inside the repository, install `pipenv`, a dependency manager for Python projects.

Install pipenv in the terminal:
```
pip install --user pipenv
```

Navigate to `rely/flaskapp/` and start virtual environment:
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

## Evaluation

To evaluate the quality and performance of the algorithms you can refer to the evaluation folder.  Simply paste any of the given functions at the bottom of a module's function for any of the four algorithms.  The output will be printed in the terminal while the local server runs.  An example is provided in the evaluation folder.
