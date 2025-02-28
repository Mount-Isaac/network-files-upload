from flask import (
    Flask,
    request,
    render_template,
    redirect,
    url_for,
    session
)
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv('secret_key', "Insecure-ThisIsSampleTestingTestingKey")
password = os.getenv('app_password', 'isaac')


app = Flask(__name__)
app.secret_key = secret_key
UPLOAD_FOLDER = '/app/uploads/data'  # Absolute path for Docker
PASSWORD = password

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('upload_file'))
        else:
            return render_template('login.html', error='Invalid password')
    return render_template('login.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', message='No file found')
        
        file = request.files.get('file')
        if file.filename == '':
            return render_template('upload.html', message='No file selected')
        
        if file:
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config.get('UPLOAD_FOLDER'), filename)
            file.save(save_path)
            print(f"File saved to: {save_path}")  # Debug print
            return render_template('upload.html', message=f"Isaac has received your file: {filename}")
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1515, debug=True)