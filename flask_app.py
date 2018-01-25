from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
@app.route("/about/")
@app.route("/services/")
@app.route("/blog/")
@app.route("/contact/")
def index():
    rule = request.url_rule
    if 'home' in rule.rule:
        return render_template("home.html")
    if 'about' in rule.rule:
        return render_template("about.html")
    if 'services' in rule.rule:
        return render_template("services.html")
    if 'blog' in rule.rule:
        return render_template("blog.html")
    if 'contact' in rule.rule:
        return render_template("contact.html")
    return render_template("home.html")

if __name__ == "__main__":
    sys.stdout = open('file.log', 'w')
    app.run()
