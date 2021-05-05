from flask import Flask, request, render_template, redirect, session, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension

# import requests

from forex_python.converter import CurrencyRates, Decimal, RatesNotAvailableError

app = Flask(__name__)

app.config['SECRET_KEY'] = "MissMillieIsGood"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

c = CurrencyRates(force_decimal=True)

@app.route('/')
def home_page():
    return render_template("base.html")

@app.route('/convert', methods=['GET'])
def convert_currency():
    '''
    Converts from one currency to another based on the amount entered

    str(c.convert('USD', 'USD', 1))
    convert from the same currency in order to test the conversions are working
    
    str(c.convert('USD', 'JPY', 100))

    str(c.convert('AAA', 'BBB', 1000))
    this one should create an error
    '''
    cur1 = request.args["cur1"]
    cur2 = request.args["cur2"]
    amount = Decimal(request.args["amount"])
    try: 
        return str(c.convert(cur1, cur2, amount))
    except:
        flash('An error occured')
        return redirect('/')
    
   
@app.route('/test')
def test_forex():
    return str(c.get_rate('USD', 'INR'))

@app.route('/test-convert')
def test_forex2():
    return str(c.convert('USD', 'INR', 10))

@app.route('/test-error')
def test_error():
    raise RatesNotAvailableError("Error")