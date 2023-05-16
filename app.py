from flask import Flask, render_template
from markers import markers

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html', markers=markers)


if __name__ == '__main__':
    app.run(debug=True)
