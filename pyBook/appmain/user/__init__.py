import sqlite3

conn = sqlite3.connect('pyBook.db') # pyBook데이터베이스에 접속, pyBook.db에 데이터베이스저장, 파일없으면 생성

cursor = conn.cursor() # 데이터베이스 커서를 가져옴
# IF NOT EXISTS조건을 붙여 user테이블이 없을 때만 생성, \는 줄바꿈을 의미
SQL = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
      ' username TEXT NOT NULL, email TEXT NOT NULL, passwd TEXT NOT NULL, authkey TEXT)'

cursor.execute(SQL) # SQL에 저장된 명령어 실행

cursor.close() # 데이터베이스 사용 후 종료
conn.close() # 데이터베이스에 접속했던 객체 종료