from flask import Flask, render_template,json
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Tiger Home Page')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')
@app.route('/base.html')
def myth1():
    return render_template('base.html')

@app.route('/cards.html')
def myth2():
    return render_template('cards.html')

@app.route('/chart4.html')
def myth4():
    return render_template('chart4.html')
@app.route('/chart5.html')
def myth5():
    return render_template('chart5.html')
@app.route('/chart6.html')
def myth6():
    return render_template('chart6.html')
@app.route('/chart7.html')
def myth7():
    return render_template('chart7.html')

@app.route("/getdata",methods=["POST","GET"])
def getdata():
    data=[{
            "x": 0,
            "y": 0,
            "width": 10,
            "height": 1,
            "div_id": "b1",
            "chart" : '/cards.html'
        },
        {
            "x": 0,
            "y": 7,
            "width": 6,
            "height": 3,
            "div_id": "3",
            "chart" : '/chart7.html'
        },
        {
            "x": 6,
            "y": 7,
            "width": 6,
            "height": 3,
            "div_id": "a2sssss",
            "chart" : '/chart6.html'
        },
        {
            "x": 6,
            "y": 4,
            "width": 6,
            "height": 3,
            "div_id": "sdfsdfa2",
            "chart" : '/chart5.html'
        },
        {
            "x": 10,
            "y": 0,
            "width": 2,
            "height": 2,
            "div_id": "2",
            "chart" : '/base.html'
        },
        {
            "x": 0,
            "y": 1,
            "width": 5,
            "height": 3,
            "div_id": "a2",
            "chart" : '/chart4.html'
        },
        {
            "x": 5,
            "y": 1,
            "width": 5,
            "height": 3,
            "div_id": "a1",
            "chart" : '/myth.html'
        },
        {
            "x": 0,
            "y": 4,
            "width": 6,
            "height": 3,
            "div_id": "1",
            "chart" :'/symbol.html'
        }]
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)

