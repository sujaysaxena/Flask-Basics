from flask import Flask, render_template, request
'''
It creates and instance of the flask class
which will be your WSGI (Web server gateway interface)
'''
##WSGI Application
app = Flask(__name__)

'''
{{    }} expression to print output in html
{%    %} conditions, loops
{#    #} comment
'''

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

#variable rule
@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    return render_template('success.html', result=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=''
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {'Score': score, 'Result': res}
    
    return render_template('successres.html', result=exp)

if __name__=="__main__":
    app.run(debug=True)