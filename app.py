from flask import Flask, session, render_template, request, flash, redirect, after_this_request
from flask_session import Session
from werkzeug.utils import secure_filename
import ocrspace
import os


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
api = ocrspace.API('e36c320cbb88957', ocrspace.Language.Arabic)
langs = [
    'Arabic',
    'Bulgarian',
    'Chinese_Simplified',
    'Chinese_Traditional',
    'Croatian',
    'Danish',
    'Dutch',
    'English',
    'Finnish',
    'French',
    'German',
    'Greek',
    'Hungarian',
    'Italian',
    'Japanese',
    'Korean',
    'Norwegian',
    'Polish',
    'Portuguese',
    'Russian',
    'Slovenian',
    'Spanish',
    'Swedish',
    'Turkish'
]

app = Flask( __name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def home(msg = None, type = 'warning'):
    if msg:
        msg = alert(msg, type)
    else:
        msg = False
    return render_template('home.html', home = 'active', langs = langs, alert = msg)


@app.route("/about", methods=["GET", "POST"])
def watt(title = None):
    if request.method == 'POST':
        a = dict(request.form)
        print(a)
        print(type(a))
    #
    return render_template('watt.html', watt = 'active' )


@app.route("/editing", methods=["GET", "POST"])
def editing(title = None):
    
    if request.method == 'POST':
        
        if 'file' not in request.files:
            return home(alert('No Image selected...!'))
        file = request.files['file']

        if file.filename == '':
            return home('No Image selected...!')
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        api = eval(f"ocrspace.API('e36c320cbb88957', ocrspace.Language.{request.form.get('lang')})")

        text = api.ocr_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        @after_this_request 
        def remove_file(response, name = full_filename): 
            os.remove(full_filename) 
            return response 

        return render_template('editing.html', text=text, file = full_filename)
    
    return home('Should upload file first!')
    

def alert(text, type='primary'):
    return {
        'msg': text,
        'type': type
    }

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

