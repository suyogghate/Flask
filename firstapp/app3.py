from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index2.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'suyog96' and password == 'password':
            return "Success"
        else:
            return "Failure"
        
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    # elif file.content_type == '.doc,.docx,.xml,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document':
    #     df = pd.read_excel(file)
    #     return df.to_html()

@app.route('/convert_csv')
def convert_csv():
    return ""

        
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)