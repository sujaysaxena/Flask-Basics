from flask import Flask, render_template, request
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

@app.route('/html')
def html_template():
    return render_template('index.html')

@app.route('/form',methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f' Hello {name}'
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)