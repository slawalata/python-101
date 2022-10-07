from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Web App with Python Flask!'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
