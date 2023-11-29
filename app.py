from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    counts = {'mentah': 10, 'kurang matang': 2, 'matang': 3, 'terlalu matang': 9}
    xArray = list(counts.keys())
    yArray = list(counts.values())
    return render_template('index.html', xArray=xArray, yArray=yArray)

if __name__ == '__main__':
    app.run(debug=True)
