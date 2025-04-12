from flask import Flask, render_template, request, send_file
import os
from huffman_compression import huffman_compression

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FILE = 'static/compressed_output.jpg'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    if 'image' not in request.files:
        return "No file part", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Call your Huffman compression function
    huffman_compression(file_path, OUTPUT_FILE)

    return send_file(OUTPUT_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
