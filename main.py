from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    if app.config['DEBUG_ENABLED']:
        app.run(port=5000, debug=True, host='127.0.0.1')
    else:
        app.run(port=80, debug=False, host='0.0.0.0')
