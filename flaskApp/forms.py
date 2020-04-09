from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class PredictForm(FlaskForm):
    stockTicker = SelectField('Stock Ticker', choices=[("TWTR", "Twitter"), ("VZ", "Verizon"), ("FB", "Facebook"), ("TSLA", "Tesla"), ("GOOGL", "Google")])
    daysToPredict = SelectField('Days', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    submit = SubmitField("Submit")

class PredictCvForm(FlaskForm):
    cVstockTicker = SelectField('Stock Ticker', choices=[("TWTR", "Twitter"), ("VZ", "Verizon"), ("FB", "Facebook"), ("TSLA", "Tesla"), ("GOOGL", "Google")])
    cVdaysToPredict = SelectField('Days', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    submit = SubmitField("Submit")

class PredictSvmForm(FlaskForm):
    svMstockTicker = SelectField('Stock Ticker', choices=[("TWTR", "Twitter"), ("VZ", "Verizon"), ("FB", "Facebook"), ("TSLA", "Tesla"), ("GOOGL", "Google")])
    svMdaysToPredict = SelectField('Days', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    submit = SubmitField("Submit")

class PredictNbForm(FlaskForm):
    nBstockTicker = SelectField('Stock Ticker', choices=[("TWTR", "Twitter"), ("VZ", "Verizon"), ("FB", "Facebook"), ("TSLA", "Tesla"), ("GOOGL", "Google")])
    nBdaysToPredict = SelectField('Days', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")])
    submit = SubmitField("Submit")
