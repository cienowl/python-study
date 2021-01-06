# MVC 중 Model 파일 내용

import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
                )


# 테이블 생성
class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)  # id 저장 정수형, PK
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # author 저장
    title = db.Column(db.Text, nullable=False)  # title 저장, Null 불가
    content = db.Column(db.Text, nullable=False)  # 내용 저장, Null 불가
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
                           backref=db.backref('posts', lazy=True))  # db.Column(db.Text)  # tags에 내용저장 null 가능

    # 편의를 위해 정의
    def __repr__(self):
        return '<Post {}>'.format(self.id)


class User(db.Model):  # Model 을 상속받음
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    account = db.Column(db.Text, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)  # 모델로만 잡혀있고 실제 칼럼으로 들어가있지 않음

    def __repr__(self):
        return '<User {}>'.format(self.id)  # lazy=Flase 면 모든 정보를 한번에 다 읽어옴


# tag helper table
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)


# DB 초기화
# @click.command('init-db')  # 사용자 정의
# @with_appcontext
def init_db():
    db.drop_all()
    db.create_all()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('DB 초기화 완료.')


def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)
