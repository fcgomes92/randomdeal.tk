from flask import Flask, redirect, render_template
from random import randint
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/rand')
def rand():
    url = get_url()
    try:
        while requests.get(url).status_code in [404, 400, 500, ]:
            url = get_url()
            # print(url)
    except Exception as e:
        print(e)
        pass
    return redirect(url)


def get_url():
    return "http://www.dx.com/{}".format(randint(0, 999999))


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
