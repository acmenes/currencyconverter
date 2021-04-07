from flask import Flask, request, render_template, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from forex_python.converter import CurrencyRates, Decimal

app = Flask(__name__)

app.config['SECRET_KEY'] = "MissMillieIsGood"
app.config['DEBUG_TB_INTERCEPT_REDIRECT'] = False
debug = DebugToolbarExtension(app)

c = CurrencyRates(force_decimal=True)

@app.route('/')
def home_page():
    return render_template("base.html")

@app.route('/convert', methods=['GET'])
def convert_currency():
    cur1 = request.args["cur1"]
    cur2 = request.args["cur2"]
    amount = Decimal(request.args["amount"])
    # return jsonify({
    #     "cur1": cur1,
    #     "cur2": cur2,
    #     "amount": Decimal(amount),
    #     "converted": str(c.convert(cur1, cur2, )
    # })
    return str(c.convert(cur1, cur2, amount))

@app.route('/test')
def test_forex():
    return str(c.get_rate('USD', 'INR'))

@app.route('/test-convert')
def test_forex2():
    return str(c.convert('USD', 'INR', 10))
