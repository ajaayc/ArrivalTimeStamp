from flask import *

app = Flask(__name__, static_url_path='')

app.config.update(
  DEBUG=True
)


@app.route("/")
def index():
    return render_template("button.html")


if __name__ == "__main__":
    app.run()
