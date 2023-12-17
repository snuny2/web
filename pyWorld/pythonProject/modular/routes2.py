from flask import Flask, send_from_directory

app = Flask(__name__)
# /로 접근시 send_from_directory()전달, 플라스크 백엔드 서버는 페이지 내용에 관여안함
@app.route('/', methods=['GET'])
def index():
    return send_from_directory(app.root_path, 'templates/index.html')
# /api/message/get로 접근시 Hello, World!전달
@app.route('/api/message/get', methods=['GET'])
def getMessage():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run('127.0.0.1', 8000)