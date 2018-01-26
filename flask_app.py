from flask import Flask, render_template, request

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
        return render_template("home.html",home=True)
    if 'about' in rule.rule:
        return render_template("about.html",about=True)
    if 'services' in rule.rule:
        return render_template("services.html",services=True)
    if 'blog' in rule.rule:
        return render_template("blog.html",blog=True)
    if 'contact' in rule.rule:
        return render_template("contact.html",contact=True)
    return render_template("home.html",home=True)

if __name__ == "__main__":
    app.run(debug=True)
