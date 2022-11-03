from flask import Flask, request
app = Flask(__name__)
@app.route('/recieve-request', methods=['POST'])
def result():
    print(request.form['foo']) # should display 'bar'
    return 'Received !' # response to your request.
