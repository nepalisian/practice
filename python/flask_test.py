from flask import Flask

app = Flask(__name__)


@app.route('/hi/<username>')
def say_hi(username):
    return "Hi %s !!" % username


@app.route('/hello/<username>')
def say_hello(username):
    return "Hello %s !!" % username


@app.route('/table')
def say_table():
    return "<table><tr><th>Firstname</th><th>Lastname</th> <th>Age</th></tr>  <tr><td>Jill</td><td>Smith</td> <td>50</td></tr></table>"