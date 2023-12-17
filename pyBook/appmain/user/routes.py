from flask import Blueprint, send_from_directory, make_response, jsonify, request # 필요한 패키지 가져옴
import sqlite3 # 데이터베이스사용을 위한 패키지 가져옴
import bcrypt  # 평문으로 된 문자열 암호화해줌

from appmain import app # 플라스크 앱 객체를 가져옴

user = Blueprint('user', __name__) # 플라스크서버에 직접설정하지 않고 user이름으로 객체를 생성하여 설정

@user.route('/signup') # /signup요청을 받으면 signUp() 실행
def signUp():
    return send_from_directory(app.root_path, 'templates/signup.html')

@user.route('/api/user/signup', methods=['POST']) # 클라이언트가 사용자데이터를 보낼 때 접속하는 주소
def register():
    data = request.form # 클라이언트의 요청을 담음
    # 키와 값의 형태로 데이터를 저장
    username = data.get("username")
    email = data.get("email")
    passwd = data.get("passwd")
    # 입력한 비밀번호는 평문으로 되어있음, 키를 전달시 해당하는 값을 반환
    hashedPW = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())

    conn = sqlite3.connect('pyBook.db') # 데이터베이스에 접속하도록 해줌
    cursor = conn.cursor() # 인덱스로 작업중인 데이터, 데이터베이스를 사용할 준비가 됬음
    # 테이블의 변경된 내용을 데이터베이스에 반영해줌
    if cursor:
        SQL = 'INSERT INTO users (username, email, passwd) VALUES (?, ?, ?)'
        cursor.execute(SQL, (username, email, hashedPW))
        conn.commit()
        # 테이블의 내용을 확인
        SQL = 'SELECT * FROM users'
        cursor.execute(SQL)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        # 사용이 끝난 뒤 종료
        cursor.close()
        conn.close()
    # 클라이언트의 요청이 정상적으로 처리됬다는 내용
    payload = {"success": True}
    return make_response(jsonify(payload), 200)