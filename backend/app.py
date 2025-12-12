# backend -> app.py
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import pymongo
from datetime import datetime

app = Flask(__name__,
             template_folder="../frontend/templates",
    static_folder="../frontend/static")

# Load environment variables
load_dotenv()

# Get MONGO URI
MONGO_URI = os.getenv('MONGO_URI')

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)

# Select database
db = client["test"]    # change "test" to your DB name

# Select collection
collection = db["Flask-tutorial"]

@app.route('/')
def landing():
    day_of_week = datetime.today().strftime('%A')
    current_date = datetime.now().strftime('%H:%M:%S')
    
    return render_template('index.html', day_of_week=day_of_week, current_date=current_date)

@app.route('/home')
def home():
    return "This is a home page"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    form_data = dict(request.form)
    collection.insert_one(form_data)
    print(name)
    return "Hello " + name + "!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
