from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='test', userName='kentei')

@app.route('/hello', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = "no name."
    return name + " Hello world!"

if __name__ == "__main__":
    app.run()