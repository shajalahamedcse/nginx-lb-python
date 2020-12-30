from flask import request, Flask
import json
app = Flask(__name__)

@app.route('/api/v1/payment/pay')
def hello_world():
    return {"msg": "hello from payment1"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)