from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='Callahan')

@app.route('/greet', methods=['GET'])
def greet():
    if 'user' in request.args:
        usr=request.args['user']
        return render_template('greet.html', user=name)
    else:
        return render_template('greet.html', user= 'Send your username with "user" in param ')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name=request.form[ 'username']
        return render_template('secure.html', user=user_name)
    else:
        return render_template('login.html')








if __name__ == "__main__":
    app.run(debug=True)