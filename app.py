from flask import Flask, request

app=Flask(__name__)
@app.route('/')

def home():
    return 'Welcome to the home page'

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