import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='owiejfn2@#$ajalkdfnalASDFAWmEKFN)_(3',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        MYSQL_DATABASE_CHARSET='utf8mb4'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)  # silent=True 는 내용을 콘솔에 찍지 말라는 내용
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    from . import db
    db.init_app(app)

    from .views import blog
    app.register_blueprint(blog)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

# 환경설정
#   pip로 설치한 패키지
#   - flask : Micro Framework
#   - sqlalchemy : ORM
#   - flask-sqlalchemy : flask에서 sqlalchemy를 더 쉽게 사용할 수 있도록 해주는 라이브러리
#   - mysql-connect-python : DBAPI 오라클에서 공식적으로 제공하는 MySSL DBAPI

#   추천하는 DB
#   - PostgresSQL : 오픈소스 DB 최신기술 적용이 빠름, 인코딩문제 없음
#   - SQLite: 가볍고 설치 간단하고 하지만 성능 딸림 기능 적음.
#   - MariaDB : MySQL 사용한 DB인데 쓸만함
#   - MySQL : 꼭 8.0 이상 사용해야 인코딩 문제 없음.

# 내장형 함수들
# pip을 통해서 깐 모듈/패키지들 pip list
# import click
# from flask import (Flask, redirect, url_for, render_template, request, session)
# from flask.cli import with_appcontext
# from flask_sqlalchemy import SQLAlchemy  # sqlalchemy는 정형화된 문법을 자동으로 쿼리문형태로 변경해서 실행해줌

# import config  # config 파일 임포트
