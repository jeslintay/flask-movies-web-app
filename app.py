from flask import Flask,url_for,redirect,request
from flask import render_template
import requests

app = Flask(__name__) 

app.config["DEBUG"] = True


@app.route("/")
def render_landing_page():
    try:
        return render_template("landing-page.html",name="Jeslin")
    except:
        return "Error occured"

@app.route("/search",methods=(['POST']))
def form_submit():
    user_query = request.form['search_query']
    redirect_url = url_for('search_imdb',query_string=user_query)
    return redirect(redirect_url)

@app.route("/search/<query_string>", methods = ["GET"])
def search_imdb(query_string):
		# This line will get our input from our HTML form from the HTML element that has 
		# the attribute name of "search_query"
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"
    querystring = {"q": query_string} # change the fixed string to video_title variable
    headers = {
        'x-rapidapi-key': "90f95a8c89msh74522d1f0ccda1bp154039jsncb5005d9cddc",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
                }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        return render_template("search-result.html", data = data)
    except:
        return render_template("error404.html")




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")