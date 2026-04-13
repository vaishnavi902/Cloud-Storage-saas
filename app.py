from flask import Flask, request, render_template_string
import os
from cryptography.fernet import Fernet

app = Flask(__name__)

# Key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Nodes (HDFS simulation)
nodes = ["node1", "node2", "node3"]

# Split file into chunks
def split_file(file, chunk_size=1024):
    chunks = []
    while True:
        data = file.read(chunk_size)
        if not data:
            break
        chunks.append(data)
    return chunks

# Merge chunks
def merge_file(output_file, total_chunks):
    with open(output_file, 'wb') as output:
        for i in range(total_chunks):
            node = nodes[i % len(nodes)]
            filename = f"{node}/chunk_{i}.bin"
            
            with open(filename, 'rb') as f:
                decrypted = cipher.decrypt(f.read())
                output.write(decrypted)

# Home page UI
@app.route('/')
def home():
    return '''
    <h2>Cloud Storage System</h2>
    
    <h3>Upload File</h3>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    
    <h3>Download File</h3>
    <form method="POST" action="/download">
        Total Chunks: <input type="number" name="chunks">
        <input type="submit" value="Download">
    </form>
    '''

# Upload route
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    chunks = split_file(file)

    for i, chunk in enumerate(chunks):
        encrypted = cipher.encrypt(chunk)
        node = nodes[i % len(nodes)]
        
        with open(f"{node}/chunk_{i}.bin", "wb") as f:
            f.write(encrypted)

    return f"File uploaded successfully! Total chunks: {len(chunks)}"

# Download route
@app.route('/download', methods=['POST'])
def download():
    total_chunks = int(request.form['chunks'])
    merge_file("output.txt", total_chunks)
    return "File downloaded successfully! Check output.txt"

# Run app
if __name__ == '__main__':
    app.run(debug=True)