from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../frontend', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/hello')
def hello():
    return {'message': 'Hello World'}

if __name__ == '__main__':
    app.run(debug=True)
