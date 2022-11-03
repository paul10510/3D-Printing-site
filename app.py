from flask import Flask, request
app = Flask(__name__)
@app.route('/recieve-request', methods=['POST'])
def result():
    file = open("database.txt",  'a')
    file.write(request.get_json.get("printRequest"))
    return 'Received !' # response to your request.

app.run()