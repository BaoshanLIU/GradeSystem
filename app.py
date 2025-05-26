from flask import Flask
from flask import Flask, render_template
from flask import request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
import os
import sys
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
app.config['SECRET_KEY'] = 'dev'  # 等同于 app.secret_key = 'dev'
db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app

# class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     name = db.Column(db.String(20))  # 名字

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(50))  # 用户名
    password_hash = db.Column(db.String(128))  # 密码散列值

    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 返回布尔值


import click


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)  # 设置密码
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)  # 设置密码
        db.session.add(user)

    db.session.commit()  # 提交数据库会话
    click.echo('Done.')

from flask_login import LoginManager

login_manager = LoginManager(app)  # 实例化扩展类
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    return user  # 返回用户对象

from flask_login import login_user

# ...

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))

        user = User.query.first()
        # 验证用户名和密码是否一致
        if username == user.username and user.validate_password(password):
            login_user(user)  # 登入用户
            flash('Login success.')
            return redirect(url_for('index_database'))  # 重定向到主页

        flash('Invalid username or password.')  # 如果验证失败，显示错误消息
        return redirect(url_for('login'))  # 重定向回登录页面

    return render_template('login.html')


from flask_login import login_required, logout_user

# ...

@app.route('/logout')
@login_required  # 用于视图保护，后面会详细介绍
def logout():
    logout_user()  # 登出用户
    flash('Goodbye.')
    return redirect(url_for('index'))  # 重定向回首页



from flask_login import login_required, current_user

# ...

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']

        if not name or len(name) > 20:
            flash('Invalid input.')
            return redirect(url_for('settings'))

        current_user.name = name
        # current_user 会返回当前登录用户的数据库记录对象
        # 等同于下面的用法
        # user = User.query.first()
        # user.name = name
        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('index'))

    return render_template('settings.html')





class Transcripts(db.Model):  # 表名将会是 Transcripts
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 课程标题
    year = db.Column(db.String(10))  # 课程年份
    Grade = db.Column(db.String(10))
    Hours = db.Column(db.String(10))
    Credits = db.Column(db.String(10))


name = 'LIU Baoshan'


Transcripts_text = [
    {'title': 'College Comprehensive English (1)', 'year': '2016 I', 'Grade': '83.4','Hours':'120','Credits':'4.0'},
    {'title': 'Advanced Mathematics I (1)', 'year': '2016 I','Grade': '92','Hours':'80','Credits':'5.0'},
    {'title': 'Mechanics', 'year': '2016 I','Grade': '98','Hours':'48','Credits':'3.0'},
    {'title': 'Fundamental Physics Experiments (1)', 'year': '2016 I','Grade': '87','Hours':'48','Credits':'1.5'},
    {'title': 'Introduction of Computer (C++ Programming)', 'year': '2016 I','Grade': '91','Hours':'64','Credits':'3.0'},
    {'title': 'Morals and Law', 'year': '2016 I','Grade': '87','Hours':'58','Credits':'3.0'},
    {'title': 'Physical Education (1)', 'year': '2016 I','Grade': '72','Hours':'32','Credits':'1.0'},
    {'title': 'Martial Training', 'year': '2016 I','Grade': 'qualified','Hours':'2 Weeks','Credits':'0.0'},
    {'title': 'College Comprehensive English (2)', 'year': '2016 II','Grade': '83.5','Hours':'120','Credits':'4.0'},
    {'title': 'Advanced Mathematics I (2)', 'year': '2016 II','Grade': '97','Hours':'80','Credits':'5.0'},
]






import click

@app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息


@app.context_processor
def inject_user():  # 函数名可以随意修改
    user = User.query.first()
    return dict(user=user)  # 需要返回字典，等同于 return {'user': user}

@app.route('/text')
def index():
    return render_template('index.html', Transcripts_text=Transcripts_text)


# #@app.route('/')
# @app.route('/', methods=['GET', 'POST'])
# def index_database():
#     #user = User.query.first()  # 读取用户记录
#     courses = Transcripts.query.all()  # 读取所有电影记录
#     return render_template('index_database.html', Transcripts=courses)

from flask_login import login_required, current_user
@app.route('/', methods=['GET', 'POST'])
def index_database():
    if request.method == 'POST':  # 判断是否是 POST 请求
        if not current_user.is_authenticated:  # 如果当前用户未认证
            return redirect(url_for('index'))  # 重定向到主页
        # 获取表单数据
        title = request.form.get('title')  # 传入表单对应输入字段的 name 值
        year = request.form.get('year')
        Credits = request.form.get('Credits')
        Hours = request.form.get('Hours')
        Grade = request.form.get('Grade')
        # 验证数据
        if not title or not year or len(year) > 10 or len(title) > 60:
            flash('Invalid input.')  # 显示错误提示
            return redirect(url_for('index_database'))  # 重定向回主页
        # 保存表单数据到数据库
        course = Transcripts(title=title, year=year, Grade=Grade, Hours=Hours, Credits=Credits)  # 创建记录
        db.session.add(course)  # 添加到数据库会话
        db.session.commit()  # 提交数据库会话
        flash('Item created.')  # 显示成功创建的提示
        return redirect(url_for('index_database'))  # 重定向回主页

    courses = Transcripts.query.all()  # 读取所有电影记录
    return render_template('index_database.html', Transcripts=courses)


@app.route('/course/edit/<int:course_id>', methods=['GET', 'POST'])
@login_required
def edit(course_id):
    course = Transcripts.query.get_or_404(course_id)

    if request.method == 'POST':  # 处理编辑表单的提交请求
        title = request.form['title']
        year = request.form['year']
        Credits = request.form['Credits']
        Hours = request.form['Hours']
        Grade = request.form['Grade']

        if not title or not year or len(year)>10 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('edit', course_id=course_id))  # 重定向回对应的编辑页面

        course.title = title  # 更新标题
        course.year = year  # 更新年份
        course.Credits = Credits
        course.Hours = Hours
        course.Grade = Grade
        db.session.commit()  # 提交数据库会话
        flash('Item updated.')
        return redirect(url_for('index_database'))  # 重定向回主页

    return render_template('edit.html', course=course)  # 传入被编辑的电影记录




@app.route('/course/delete/<int:course_id>', methods=['POST'])  # 限定只接受 POST 请求
@login_required  # 登录保护
def delete(course_id):
    course = Transcripts.query.get_or_404(course_id)  # 获取电影记录
    db.session.delete(course)  # 删除对应的记录
    db.session.commit()  # 提交数据库会话
    flash('Item deleted.')
    return redirect(url_for('index_database'))  # 重定向回主页





# 添加命令行命令：写入数据
@app.cli.command()
def forge():
    """写入成绩数据到数据库"""
    db.create_all()  # 确保表存在

    name = 'LIU Baoshan'
    Transcripts_data = [
        {'title': 'Advanced Mathematics I (1)', 'year': '2016 I','Grade': '92','Hours':'80','Credits':'5.0'},
        {'title': 'Mechanics', 'year': '2016 I','Grade': '98','Hours':'48','Credits':'3.0'},
        {'title': 'Fundamental Physics Experiments (1)', 'year': '2016 I','Grade': '87','Hours':'48','Credits':'1.5'},
        {'title': 'Introduction of Computer (C++ Programming)', 'year': '2016 I','Grade': '91','Hours':'64','Credits':'3.0'},
        {'title': 'Morals and Law', 'year': '2016 I','Grade': '87','Hours':'58','Credits':'3.0'},
        {'title': 'Physical Education (1)', 'year': '2016 I','Grade': '72','Hours':'32','Credits':'1.0'},
        {'title': 'Martial Training', 'year': '2016 I','Grade': 'qualified','Hours':'2 Weeks','Credits':'0.0'},
        {'title': 'College Comprehensive English (2)', 'year': '2016 II','Grade': '83.5','Hours':'120','Credits':'4.0'},
        {'title': 'Advanced Mathematics I (2)', 'year': '2016 II','Grade': '97','Hours':'80','Credits':'5.0'},
    ]

    # 添加用户
    user = User(name=name)
    db.session.add(user)

    # 添加所有课程
    for item in Transcripts_data:
        transcript = Transcripts(
            title=item['title'],
            year=item['year'],
            Grade=item['Grade'],
            Hours=item['Hours'],
            Credits=item['Credits']
        )
        db.session.add(transcript)

    db.session.commit()
    click.echo('成绩数据已成功写入数据库！')

# 路由和其他现有代码保持不变...


@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    #user = User.query.first()
    return render_template('404.html'), 404  # 返回模板和状态码