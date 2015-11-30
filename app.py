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
        for r in results:
            rlist.append(r)
        url = urllib2.urlopen(rlist[0])
        page = url.read()
        soup = bs4.BeautifulSoup(page,'html5lib')
        raw = soup.get_text()
        #text = re.sub("[ \t\n]+"," ",raw)
        text = raw
        #print text
        return render_template("home.html", query=q, results=results)
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

