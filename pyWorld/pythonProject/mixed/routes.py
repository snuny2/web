from flask import Flask, render_template # Flask패키지에서 클래스 가져옴

app = Flask(__name__) # Flask클래스를 app에 할당, __name__를 이용해 객체이름 지정

@app.route('/',methods=['Get']) # 파이썬 데커레이터, 아래에 있는 코드(index.html)를 감쌈(데커레이터 > 코드 > 데커레이터)
def index(): # 템플릿, 데이터를 채운뒤 페이지를 요청한 클라이언트에게 전달하는 플라스크 함수
    return render_template('index.html', message='Hello World!')

if __name__== '__main__': # 직접 실행되는 주요프로그램이라는 의미를 줌
    app.run('127.0.0.1', 8000)