from flask import Flask, request, render_template, send_from_directory
import os


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return send_from_directory('static', 'opening.html')

@app.route('/upload', methods=['POST'])
def upload_picture():
    print(request.files)
    if 'file' not in request.files:
        return 'No file found', 400
    

    file = request.files['file']

    if file.filename == '':
        return 'No file selected', 400
    
    if not os.path.exists('./static/images'):
        os.makedirs('./static/images')

    file.save('./static/images/' + file.filename)

    results = do_stuff_with_picture(file.filename)
    return render_template('picture.html', picture_path='./static/images/' + file.filename, information=results )
    


def do_stuff_with_picture(filename):
    results = "Basic information about the image, cool AI stuff"
    return results

if __name__ == '__main__':
    app.run()