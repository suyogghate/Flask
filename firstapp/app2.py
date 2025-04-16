from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    name='Suyog Ghate'
    age=30
    my_list = [10, 20, 30, 40]
    return render_template('index.html', name=name, age=age, my_list=my_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)