from flask import Flask, render_template
from markers import markers

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html', markers=markers)


@app.route('/landmark/<name>')
def landmark(name):
    # Find the landmark with the given name
    place = next((marker for marker in markers if marker['name'].lower().replace(" ", "-") == name), None)

    if place:
        return render_template('landmark.html', landmark=place)
    else:
        return 'Landmark not found'


if __name__ == '__main__':
    app.run(debug=True)
