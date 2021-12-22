from flask import Flask, render_template, request, redirect, url_for
from coingecko import get_price
import db_work

app = Flask(__name__)

@app.route('/wallet/<login>')
def wallet(login):
    print(login)
    temp=db_work.get_invests(login)
    print(temp)
    if type(temp) == type("string"):
        return(render_template("home.html", login=login, addassets=temp))
    else:
        assets = []
        pnl_all = 0
        deposit = 0
        balance = 0
        for cur in temp:
            curprice = float(get_price(cur[0]))
            curvalue = curprice*float(cur[1])
            pnl = curvalue-float(cur[3])
            pnl_percent = (pnl/float(cur[3]))*100
            assets.append({'title':cur[0], 'amount':cur[1], 'price':cur[2], 'curprice':str(curprice), 'value':cur[3],
                           'curvalue':str(curvalue), 'pnl':pnl, 'pnl_percent':pnl_percent})
            pnl_all += pnl
            deposit += float(cur[3])
            balance += curvalue
        pnl_percent_all = (balance/deposit-1)*100
        return(render_template("home.html", login=login, tokens=assets, balance=balance, deposit=deposit, pnl=pnl_all, pnl_percent=pnl_percent_all))

@app.route('/')
def hello():
    return(render_template("index.html"))

@app.route('/handle_data_signin', methods=['POST'])
def handle_data_signin():
    login = request.form['data_signin_login']
    email = request.form['data_signin_email']
    pswrd = request.form['data_signin_pswrd']
    response = db_work.add_user(login, email, pswrd)
    if not response:
        return redirect(url_for('wallet', login=login))
    else:
        return render_template("index.html", warn = response)

@app.route('/handle_data_login', methods=['POST'])
def handle_data_login():
    login = request.form['data_login_login']
    pswrd = request.form['data_login_pswrd']
    response = db_work.find_user(login, pswrd)
    if not response:
        return redirect(url_for('wallet', login=login))
    else:
        return render_template("index.html", warn = response)

@app.route('/add_assets', methods=['POST'])
def add_assets():
    login = request.form['addcur_login']
    title = request.form['addcur_cur']
    amount = request.form['addcur_amount']
    price = request.form['addcur_price']
    response = db_work.add_assets(login, title, amount, price)
    if not response:
        return redirect(url_for('wallet', login=login))
    else:
        return redirect(url_for('wallet', login=login))

app.run()