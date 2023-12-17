# route() 데커레이터, 전달된 경로에 HTTP요청이 들어왔을 때 먼저 호출
from flask import Blueprint, send_from_directory
from appmain import app

main = Blueprint('main', __name__) # main이라는 객체생성

# /와 /home에 접속했을때 서버가 해야할 동작을 정의
@main.route('/')
@main.route('/home')
def home():
    return send_from_directory(app.root_path, 'templates/index.html')