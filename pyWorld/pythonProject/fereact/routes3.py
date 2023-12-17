from flask import Flask, send_from_directiry

app = Flask(__name__, static_folder='build', static_url_path='/')

@app.route('/', methods=["GET"])
def index():
    return send_from_directiry('build', 'index.html') # 프런트엔드 코드를 클라이언트에게 전달

@app.route('/api/message/get', methods=["GET"])
def getMessage():
    return 'Hello World!'

if __name__ == '__main__':
    app.run('127.0.0.1', 8000)