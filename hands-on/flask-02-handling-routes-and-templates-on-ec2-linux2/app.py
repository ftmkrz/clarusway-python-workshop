from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is home page for no path, <h1> Welcome Home </h1>'

@app.route('/about')
def about():
    return '<h1> This is my about page </h1>'

@app.route('/error')
def error():
    return '<h1> Either you encountered an error or you are not authorized.<h1>' 


@app.route('/hello')
def hello():
    return '<h1> Hello, World! <h1>'


@app.route('/admin')
def admin():
    return redirect(url_for('error'))




@app.route('/greet_admin')
def greet_admin():
    return redirect(url_for('greet', name='Master Admin!!!'))



@app.route('/<username>')
def greet(username):
    return render_template('greet.html', name=username)



@app.route('/list10')
def list10():
    return render_template('list10.html')

@app.route('/evens')
def evens():
    return render_template('evens.html')



    









if __name__ == "__main__":

    #app.run(debug=True)
    app.run('0.0.0.0', port=80)
        




   
 
