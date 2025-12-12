# backend -> app.py
from flask import Flask, render_template
from datetime import datetime
import requests

BACKEND_URL = 'https://0.0.0.0'

app = Flask(__name__,
             template_folder="../frontend/templates",
    static_folder="../frontend/static")

@app.route('/')
def landing():
    day_of_week = datetime.today().strftime('%A')
    current_date = datetime.now().strftime('%H:%M:%S')
    
    return render_template('index.html', day_of_week=day_of_week, current_date=current_date)

@app.route('/home')
def home():
    return "This is a home page"

@app.route('/get-data')
def getdata():
    response = requests.get(BACKEND_URL + '/submit')
    data = response.json
    return data