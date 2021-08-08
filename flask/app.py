from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/hello')
def hello():
    return {
        "a": 123,
        "b": 456,
    }

@app.route('/func')
def func():
    return 'welcome! func!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
