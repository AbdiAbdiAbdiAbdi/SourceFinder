from flask import Flask, request, jsonify
from flask_cors import CORS
from news import News_Getter
from emailer import send_email

app = Flask(__name__)
CORS(app)



@app.route('/news')
def news():
    return News_Getter("Investments")

@app.route('/api/text', methods=['POST'])
def receive_text():
    #Parse the JSON data from request
    data = request.get_json()
    text = data.get('text')
    email = data.get('email')
    print(f"Received text: {text}")
    print(f"Received email: {email}")
    return jsonify(send_email(text, email))

if __name__ == "__main__":
    app.run(debug=True)