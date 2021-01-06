# import math
# math.cos()
# from math import cos    #cos만 쓸경우 math를 import 하는건 낭비
# cos()

# 내장형 함수들
# pip을 통해서 깐 모듈/패키지들

from flask import (Flask, redirect, url_for, render_template, request)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:34811005@localhost/blog'

db = SQLAlchemy(app)

#테이블 생성
class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)    #id 저장 정수형, PK
    title = db.Column(db.Text, nullable=False)  #title 저장, Null 불가
    content = db.Column(db.Text, nullable=False)    #내용 저장, Null 불가
    tags = db.Column(db.Text)       #tags에 내용저장 null 가능

    def __init__(self, title, content, tags):   #self는 this와 같음 꼭 명시적으로 작성해야함
        self.title = title
        self.content = content
        self.tags = tags

    #편의를 위해 정의
    def __repr__(self):
        return '<Post {}>'.format(self.id)

db.drop_all()   #만약 같은 테이블이 있으면 갈아엎음
db.create_all() #테이블을 만듦





@app.route('/') #/주소표시줄 내용
                #첫 페이지는 index
def index():    #"""은 여러줄
    # return  """
    #     <html>
    #     <body><h1>이건 제목</h1></body>
    #     </html>
    # """
    return render_template(
        "index.html",
        title = "Flask를 배워보자",
        content = "Flask가 이렇게 쉽습니다.",
        comments=['댓글1', '댓글2', '댓글3', '댓글4', '댓글5']
    )

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/register',methods=['GET', 'POST']) #기본적으로 get만 작동 그래서 methods를 써줘야함
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':  # 현재 GET 아니면 POST니까 else로 해도 무방
        # 여기서 회원가입 정보를 서버에 저장

        return redirect(url_for('index'))   #회원가입 내용 서버에 저장하고 index 페이지로 이동


@app.route('/hello/<var1>')    #/hello 주소표시줄 내용 <> 안에는 변수로 인식
def hello_world(var1):
    return "Hello, {}!.format(var1)"

#127.0.0.5:5000/2018/03/10/learning-flask-2/
@app.route('/<int:year>/<int:month>/<int:day>/<string:title>/')
def learning_flask(year,month,day,title):
    # 연, 월, 일, 글제목 받은 데이터로 DB에서 글을 꺼내옴
    # year, month, day, title
    return "{}/{}/{} title:{}".format(year,month,day,title)



@app.route('/hello2')   #/hello2 주소로 가면 root url 로 리디렉션
def redirect_to_hello():
    return redirect(
        url_for("hello_world",name="de")   #url_for를 사용해서 index 페이지로 이동, 매개변수도 가져가려면 변수에 대입해서 보냄
    )

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'GET':
        return render_template('write.html')
    else:   #POST 형식이 왔을 때
        title = request.form['title']
        content = request.form['content']
        tags = request.form['tags']
        #TODO: DATABASE에 저장



# 유저가 직접 이파일을 실행하면 이 파일이 main 이다. flask에서 안써도됨.
# if __name__ == '__main__':  #위에가 main함수이면 app을 실행 java에서 public static main 같은 아이
#     app.run()

# 매우 중요!!! (terminal에서 실행하는 내용)
# flask run : 플라스크 실행
# set FLASK_APP = flask_hello.py : flask_hello.py 파일이 실행될때 자동으로 main으로 실행
# set FLASK_ENV=development : 내 컴퓨터를 development 환경으로 지정해서 코드가 변화할때마다 재실행
# 배포시에는 위 라인 작성시 해킹의 위험이 있음. (기본값은 production)

# 0609
# HTML
# flask의 HTML template (render_template()과 url_for())
# redirect