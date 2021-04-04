from flask import Flask, json
from import_controller.exante_controller import Exante

app = Flask(__name__)


@app.route('/')
def view():
    return 'Hello, World!'


@app.route('/transactions')
def transactions():
    account = Exante()
    transactions = account.import_from_external_source()
    a = []
    for t in transactions:
        a.append(t.serialize())
    return json.jsonify(a)


if __name__ == '__main__':
    app.run()
