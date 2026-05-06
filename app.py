from flask import Flask

app=Flask(__name__)
@app.route('/')

def home():
    return 'Welcome to the home page'

@app.route('/api/<name>')
def name(name):
    length=len(name)
    if length>5:
        return 'Name is too long'
    else:
        return 'Nice name...'+name
    
if __name__ =='__main__':
    app.run(debug=True)