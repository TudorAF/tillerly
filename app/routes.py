from app import app
from flask import render_template
from app.models import TillerTransactions


@app.route('/')
@app.route('/index')
def index():
    tiller_transacs = [ {'date' :'2019/01/01',
                         'description' :'blah',
                         'category_hint' : 'Test',
                         'account_number' : '2032',
                         'amount' : '00' } ,
                        {'date': '2018/01/01',
                         'description': 'test 2',
                         'category_hint': 'ass',
                         'account_number': '1111',
                         'amount': 999} ]

    print (tiller_transacs)
    return render_template("transactions.html", transactions=tiller_transacs)