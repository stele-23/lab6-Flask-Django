from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Welcome to Flask!</h2><p><a href="/form">Go to form</a></p>'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', '').strip()
    if not name:
        return redirect(url_for('form'))
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)

