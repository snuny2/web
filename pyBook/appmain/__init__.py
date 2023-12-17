from flask import Flask

app = Flask(__name__) # 객체생성

from appmain.routes import main # routes.py파일에서 Blueprint객체인 main을 불러옴
app.register_blueprint(main) # Blueprint객체를 register_blueprint()를 이용하여 FLask객체에 등록
# user객체를 가져와 등록
from appmain.user.routes import user
app.register_blueprint(user)