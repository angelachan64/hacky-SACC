from flask import Flask, render_template,redirect, request, session, url_for
import urllib2, json, google, bs4, re
import googleapi

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
    if request.method == "POST":
        q = request.form['query']
        results = google.search(q, num=10, start=0, stop=10)
        rlist = []
        for r in range(10):
            rlist.append(results.next())
        hlist = []
        for r in range(10):
            hlist.append(googleapi.getHTML(rlist[r]));
        return render_template("home.html", query=q, results=rlist, htmls=hlist)
    else:
        return render_template("home.html")
    
@app.route("/results")
def results():
    return render_template("results.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
   app.debug = True
   app.secret_key = "shh"
   app.run(host="0.0.0.0", port=8000)

