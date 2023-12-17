import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

SQL = 'INSERT INTO users (username, email, password) VALUES (?, ?, ?)' # INSERT명령어 사용
cursor.execute(SQL, ('admin', 'admin@abc.com', 'imsi_00')) # 순서대로 데이터 전달
conn.commit() # 지금까지 변경된 내용들을 반영해줌

SQL = 'SELECT * FROM users' # SELECT명령어 입력
cursor.execute(SQL) # execute()함수를 이용하여 실행
rows = cursor.fetchall() # 실행한 결과 저장, cursor이 가지고있는 결과 반환
# 배열형태의 변수에 저장, for문을 이용해서 행마다 내용출력
for row in rows:
    print(rows)

SQL = 'PRAGMA table_info(users)' # PRAGMA명령어 입력, 테이블구조 출력
cursor.execute(SQL) # execute()함수를 이용하여 실행
rows = cursor.fetchall() # 실행한 결과 저장
# for문을 이용해서 각 요소의 내용출력
for row in rows:
    print(rows)
# 사용을 마친뒤 종료
cursor.close()
conn.close()