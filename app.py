from flask import Flask
'''
It creates and instance of the flask class
which will be your WSGI (Web server gateway interface)
'''
##WSGI Application
app = Flask(__name__)

@app.route('/')
def sample_flask_app():
    return "Welcome to the Flask Application"

@app.route('/index')
def sample_index():
    return "Welcome to the index of the flask app"

if __name__=="__main__":
    app.run(debug=True)