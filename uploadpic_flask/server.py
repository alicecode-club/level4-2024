from flask import Flask, request, render_template
import os


app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_picture():
    print(request.files)
    if 'file' not in request.files:
        return 'No file found', 400

    file = request.files['file']

    if file.filename == '':
        return 'No file selected', 400
    

    file.save('./static/' + file.filename)

    results = do_stuff_with_picture(file.filename)
    return render_template('picture.html', picture_path='./static/' + file.filename, information=results)


#here you should do the picture processing
def do_stuff_with_picture(filename):
    results = "Basic information about the image, cool AI stuff"
    return results

if __name__ == '__main__':
    app.run()