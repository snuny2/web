from appmain import app # Flask객체인 app가져옴

if __name__ == '__main__': # 다른 스크립트에 포함, 인프리터에 의해 직접호출되어 실행
    app.run('127.0.0.1', 8000) # ip주소, 포트번호