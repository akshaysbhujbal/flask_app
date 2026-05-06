from flask import Flask

app=Flask(__name__)
@app.route('/')

def home():
    return 'Welcome to the home page'

#Value get from url
'''@app.route('/api/<name>')
def name(name):
    length=len(name)
    if length>5:
        return 'Name is too long'
    else:
        return 'Nice name...'+name'''


#addition of two number ie get from url
@app.route('/add/<a>/<b>')
def add(a,b):
    answer=int(a)+int(b)
    result={'ans':answer}
    return result
if __name__ =='__main__':
    app.run(debug=True)