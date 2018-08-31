# accuweather keys
# location key (for foxford)= 210463
# API key = pc2TdWiYE3WoXW0xP339FGj8HWqXpeEc


from flask import Flask, render_template, redirect, request
import urllib, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("template.html")

@app.route('/weather', methods = ["GET", "POST"])
def getweather():
    if request.method == "POST":
        print("entered loop")
        url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/210463?apikey=pc2TdWiYE3WoXW0xP339FGj8HWqXpeEc'
        
        response = request.get(url)
        jresponse = response.text
        data = json.loads(jresponse)
        print(data)
        a = "Jennifer is great"
        return render_template("template.html",  a=a)
    else:
        print("entered else loop")
        render_template("template.html")

if __name__ == "__main__":
    app.run(debug= True)



