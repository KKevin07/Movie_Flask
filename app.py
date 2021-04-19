from flask import  Flask,render_template,request
import  datetime
import  sqlite3
app = Flask(__name__)

FLASK_DEBUG=1


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/index')
def home():
    return index()
@app.route('/MovieDataNumber')
def MovieDataNumber():
    datalist = []
    con = sqlite3.connect("Douban_movie_Top250.db")
    cur = con.cursor()
    sql = "select * from DoubanMovieTop250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()

    return render_template("MovieDataNumber.html",movies = datalist)

@app.route('/MovieWebNumber')
def MovieWebNumber():
    return render_template("MovieWebNumber.html")

@app.route('/RatingNumber')
def RatingNumber():
    return render_template("RatingNumber.html")

@app.route('/WordFrequency')
def WordFrequency():
    return render_template("WordFrequency.html")





if __name__ == '__main__':
    app.run(debug=True)       #web默认运行在本机地址：http://127.0.0.1:5000/