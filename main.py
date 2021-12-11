from flask import Flask, request, render_template, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import os
import predict


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        img = request.files['image']

        # Save image
        filename = secure_filename(img.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        img.save(path)

        prediction = predict.predict(path)

        # Save image in static for website
        img.seek(0)
        path2 = os.path.join('./static/uploads', filename)
        img.save(path2)

        return render_template('result.html', prediction=prediction, path='uploads/'+filename)

    # Homepagina
    return render_template('index.html')


app.run(host='127.0.0.1', port=8080, debug=True)
