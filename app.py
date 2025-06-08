from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    if request.method == 'POST':
        file = request.files['image']
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            img = Image.open(path)
            lang = request.form.get('lang', 'heb')
            psm = request.form.get('psm', '3')
            config = f'--psm {psm}'
            text = pytesseract.image_to_string(img, lang=lang, config=config)
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    if request.method == 'POST':
        file = request.files['image']
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            img = Image.open(path)
            text = pytesseract.image_to_string(img, lang='heb')
    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

