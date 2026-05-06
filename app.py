from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv
import os
from pymongo import MongoClient
load_dotenv()
MONGO_URI=os.getenv("MONGO_URI")

client=MongoClient(MONGO_URI)
print("MONGO_URI:", MONGO_URI)
db=client.test
collection=db['users']

#client=mongodb+srv://akshaysb:25980@asbcluster.g7sfjqn.mongodb.net/?appName=asbCluster

app=Flask(__name__)
@app.route('/')
def home():
    day_of_week=datetime.today().strftime('%A')
    current_time=datetime.now().strftime('%H:%M:%S')
    return render_template('index.html',day_of_week=day_of_week,current_time=current_time)
    #return {'day':day_of_week, 'time':current_time}
    
@app.route('/submit', methods=['POST'])    
def submit():
    form_data=dict(request.form)
    collection.insert_one(form_data)
    return 'Registered successfully!'
#Value get from url 
@app.route('/api/<name>') #User needs to send like '5000/name/Sam'
def name(name):
    length=len(name)
    if length>5:
        return 'Name is too long'
    else:
        return 'Nice name...'+name

#Value get from request -- to do so import request from flask
@app.route('/api/check') #User needs to send like 5000/api/check?name=Samantha&age=26
def check():
    name=request.args.get('name')
    age=request.args.get('age')
    age=int(age)

    if age>18:
        return 'Welcome to the site '+ name+'!'
    else:
        return 'Sorry, you are too young to use this site'

#addition of two number ie get from url  
@app.route('/add/<a>/<b>') #User needs to send like 5000/add/89/8 
def add(a,b):
    answer=int(a)+int(b)
    result={'ans':answer}
    return result
if __name__ =='__main__':
    app.run(debug=True)