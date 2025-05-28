from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from gradesystem import db



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(50))  # 用户名
    password_hash = db.Column(db.String(128))  # 密码散列值

    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 返回布尔值

class Transcripts(db.Model):  # 表名将会是 Transcripts
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 课程标题
    year = db.Column(db.String(10))  # 课程年份
    Grade = db.Column(db.String(10))
    Hours = db.Column(db.String(10))
    Credits = db.Column(db.String(10))


class Transcripts_ucas(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 课程标题
    year = db.Column(db.String(10))  # 课程年份
    Grade = db.Column(db.String(10))
    Hours = db.Column(db.String(10))
    Credits = db.Column(db.String(10))


class Transcripts_cityuhk(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    Code = db.Column(db.String(10))
    title = db.Column(db.String(60))  # 课程标题
    year = db.Column(db.String(10))  # 课程年份
    Grade = db.Column(db.String(10))
    Credits = db.Column(db.String(10))

class Transcripts_polyuhk(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    Code = db.Column(db.String(10))
    title = db.Column(db.String(60))  # 课程标题
    year = db.Column(db.String(10))  # 课程年份
    Grade = db.Column(db.String(10))
    Credits = db.Column(db.String(10))