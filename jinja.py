from flask import Flask, render_template, request, redirect, url_for
'''
It creates and instance of the flask class
which will be your WSGI (Web server gateway interface)
'''
##WSGI Application
app = Flask(__name__)

'''
{{    }} expression to print output in html
{%    %} conditions, loops
{#     #}
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

#variable rule
#for loop with key-value pair
@app.route('/successres/<int:score>')
def successres(score):
    res=''
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {"score":score, "result":res}
    
    return render_template('successres.html', result=exp)

#variable rule
#ifelse
@app.route('/successifelse/<int:score>')
def successifelse(score):
    
    return render_template('successifelse.html', result=score)

#dynamic url (one html page will call another)
@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method=='POST':
        Science = float(request.form['science'])
        math = float(request.form['math'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score = (Science+math+c+datascience)/4
        return redirect(url_for('successres',score=total_score))
    
    return render_template('submit.html')


if __name__=="__main__":
    app.run(debug=True)