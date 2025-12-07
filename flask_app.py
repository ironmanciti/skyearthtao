from flask import Flask, render_template, request, make_response

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

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    urls = [
        'http://www.1000ji.co.kr/home/',
        'http://www.1000ji.co.kr/about/',
        'http://www.1000ji.co.kr/services/',
        'http://www.1000ji.co.kr/contact/'
    ]

    sitemap_xml = render_template('sitemap.xml', urls=urls)
    response = make_response(sitemap_xml)
    response.headers['Content-Type'] = 'application/xml'

    return response

if __name__ == "__main__":
    app.run(debug=True)
