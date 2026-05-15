from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient
load_dotenv()
MONGO_URI=os.getenv("MONGO_URI")

client=MongoClient(MONGO_URI)
print("MONGO_URI:", MONGO_URI)

db = client["akshay"]
collection = db["users"]
app=Flask(__name__)
    
@app.route('/submit', methods=['POST'])    
def submit():
    form_data=dict(request.form)
    collection.insert_one(form_data)
    return 'Registered successfully!'
    

@app.route('/view')
def view():
    data=collection.find()
    data=list(data)
    for item in data:
        del item['_id']
        print(item)
    data={
        'data':data
    }
    return jsonify(data)
 
if __name__ =='__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)