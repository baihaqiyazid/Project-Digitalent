from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        speedAvg = request.form['speedAvg']
        speedStd = request.form['speedStd']
        secondZone = request.form['secondZone']
        return render_template('show.html', 
                                speedAvg=speedAvg,
                                speedStd=speedStd,
                                secondZone=secondZone)
    say = "Hello World"
    say2 = "Hello say"
    return render_template('index.html',  say=say, say2=say2)

if __name__ == '__main__':
    app.run(debug=True)