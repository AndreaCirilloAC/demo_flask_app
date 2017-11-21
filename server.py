# importo una libreria
from flask import Flask, request
# creare una istanza dell'oggetto Flask
app = Flask("BigDive")

# comunico la rotta INDEX

@app.route('/', methods=['get','post'])
def index():
    print 'Sono in INDEX'
    if request.method == 'POST':
        return 'POST METHOD'
        data = request.form
    else:
        return 'GET METHOD'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name ='pippo'):
    return 'Hello %s' %name

@app.route('/somma/<int:X>/<int:Y>')
def somma(X,Y):
    return 'Somma %s' % (X+Y)

@app.route('/brutta_storia')
def rimostranze():
    return "chi ti ha detto di venire qui?"

@app.route('/nonmivedi')
def nonmivedi():
    return redirect('/')


app.run()
