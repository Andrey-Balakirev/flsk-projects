from flask import Flask
from weather import weather_by_city
from flask import render_template
import requests
app = Flask(__name__)


@app.route('/')
def index():
    data = weather_by_city("Moscow,Russia")
    return render_template('index.html', weather=data)
    

if __name__=="__main__":
    app.run()
