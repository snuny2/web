import sqlite3 # sqlite3패키지를 가져옴

conn = sqlite3.connect("test.db") # test.db라는 이름의 데이터베이스 생성
cursor = conn.cursor() # 커서, 인덱스를 관리하는 객체

SQL = 'CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL)'
# SQL명령어

cursor.execute(SQL) # execute()를 이용하여 SQL변수에 저장된 명령어 실행

# 사용한 후 접속 해제, 해제해야 다른 프로그램에 문제없음
cursor.close()
conn.close()