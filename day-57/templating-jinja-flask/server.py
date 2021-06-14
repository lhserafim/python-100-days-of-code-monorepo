from flask import Flask, render_template
import random
import datetime as dt
from apis import AgifyAndGenderize
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = dt.datetime.now().year
    return render_template("index.html", num=random_number, year=year)  # passando parâmetros p/ o template


@app.route("/guess/<name>")
def guess(name):
    api = AgifyAndGenderize(name)
    gender = api.get_genderize()
    age = api.get_agify()
    return render_template("guess.html", name=name.capitalize(), gender=gender, age=age)


@app.route("/blog/<int:num>")  # converti p/ int p/ poder tratar no html
def blog(num):
    blog_url = "https://api.npoint.io/d1bf2629a7f09661962d"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)