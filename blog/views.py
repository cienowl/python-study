# MVC 중 Controller 파일 내용

from flask import Blueprint, render_template, redirect, request, url_for, session

from .db import db, User, Post, Tag

blog = Blueprint('blog', __name__, template_folder='templates')

@blog.route('/')  # /주소표시줄 내용
# 첫 페이지는 index
def index():  # """은 여러줄
    # return  """
    #     <html>
    #     <body><h1>이건 제목</h1></body>
    #     </html>
    # """
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@blog.route('/about')
def about():
    return render_template("about.html")


@blog.route('/register', methods=['GET', 'POST'])  # 기본적으로 get만 작동 그래서 methods를 써줘야함
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':  # 현재 GET 아니면 POST니까 else로 해도 무방
        name = request.form["name"]
        password = request.form["password"]
        account = request.form["account"]

        new_user = User(name=name, password=password, account=account)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('blog.index'))  # 회원가입 내용 서버에 저장하고 index 페이지로 이동


# @blog.route('/hello/<var1>')  # /hello 주소표시줄 내용 <> 안에는 변수로 인식
# def hello_world(var1):
#     return "Hello, {}!.format(var1)"


# 127.0.0.5:5000/2018/03/10/learning-flask-2/
# @blog.route('/<int:year>/<int:month>/<int:day>/<string:title>/')
# def learning_flask(year, month, day, title):
#     # 연, 월, 일, 글제목 받은 데이터로 DB에서 글을 꺼내옴
#     # year, month, day, title
#     return "{}/{}/{} title:{}".format(year, month, day, title)


# @blog.route('/hello2')  # /hello2 주소로 가면 root url 로 리디렉션
# def redirect_to_hello():
#     return redirect(
#         url_for("hello_world", name="de")  # url_for를 사용해서 index 페이지로 이동, 매개변수도 가져가려면 변수에 대입해서 보냄
#     )


@blog.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'GET':
        if not session.get('logged_in'):     # logged_in 이라는 key로 세션이 설정되어있는지 확인 .get은 해당 key값이 없으면 None으로 뜸 예외처리 하지 않아도 됨.
            return redirect(url_for('blog.login'))
        return render_template('write.html')
    else:  # POST 형식이 왔을 때
        title = request.form['title']
        content = request.form['content']
        tags = request.form['tags']
        if tags:
            # tag_list = []
            # fot tag in tags.split(' '):
            #     tag_list.append(Tag(name=tag))
            tag_list = [Tag(name=tag) for tag in tags.split(' ')]

        # TODO: DATABASE에 저장
        p = Post(author_id=1, title=title, content=content,
                 tags=tag_list)  # 같은 컨택스트(문맥)로 묶어서 보내서 오류를 없애야함. 값이 분리되는 경우 대형사고
        p.author = User.query.filter_by(id=session['user_id']).first()   # 로그인한 사람이 글쓴이로 들어감
        db.session.add(p)  # 준비 상태
        db.session.commit()  # sql이 실행되면서 실제 데이터가 들어감.

        return redirect(url_for('blog.index'))


@blog.route('/post/<post_id>/update')
def get_update(post_id):
    if not session.get('logged_in'):
        return redirect(url_for('blog.login'))
    p = Post.query.filter_by(id=post_id).first()

    return render_template('update.html', post=p)


@blog.route('/update', methods=['post'])
def update():
    post_id = request.form['post_id']
    title = request.form['title']
    content = request.form['content']
    tags = request.form['tags']
    if tags:
        tag_list = [Tag(name=tag) for tag in tags.split(' ')]

    p = Post.query.filter_by(id=post_id).first()
    p.title = title
    p.content = content
    p.tags = tag_list
    db.session.commit()

    return redirect(url_for('blog.get_post', post_id=p.id))


@blog.route('/post/<post_id>/delete', methods=['DELETE'])
def delete(post_id):
    p = Post.query.filter_by(id=post_id).first()
    db.session.delete(p)
    db.session.commit()

    return redirect(url_for('blog.index'))


@blog.route('/post/<post_id>')
def get_post(post_id):
    p = Post.query.filter_by(id=post_id).first()  # .first()는 처음 한개만 가져욤, .all()은 전부 가져옴

    return render_template("post.html", post=p)


@blog.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(account=username).first()    #SELECT table_name.col1, table_name.col2, table_name.col3 from table_name;

        if user is not None and str(user.password) == password:   #user의 password와 account를 가져와서 비교
            session['logged_in'] = True
            session['user_id'] = user.id
            return redirect(url_for('blog.index'))   #로그인 성공시 index 페이지로 이동
        else:
            return redirect(url_for('blog.login'))   #로그인 실패시 login 으로 다시 이동


@blog.route('/logout', methods=['POST'])
def log_out():
    if session.get('logged_in'):    # 로그인 되어있을 때만 실행
        session['logged_in'] = False
        del session['user_id']

    return redirect(url_for('blog.index'))

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
