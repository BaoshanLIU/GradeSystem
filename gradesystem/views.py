# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user

from gradesystem import app, db
from gradesystem.models import User, Transcripts, Transcripts_ucas, Transcripts_cityuhk, Transcripts_polyuhk

from flask_login import login_required, current_user


#山大成绩单的主视图
@app.route('/sdu', methods=['GET', 'POST'])
def index_database():
    if request.method == 'POST':  # 判断是否是 POST 请求
        if not current_user.is_authenticated:  # 如果当前用户未认证
            return redirect(url_for('index_database'))  # 重定向到主页
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









#山大成绩单的修改成绩视图
@app.route('/sdu/course/edit/<int:course_id>', methods=['GET', 'POST'])
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


#山大成绩单的删除视图
@app.route('/sdu/course/delete/<int:course_id>', methods=['POST'])  # 限定只接受 POST 请求
@login_required  # 登录保护
def delete(course_id):
    course = Transcripts.query.get_or_404(course_id)  # 获取电影记录
    db.session.delete(course)  # 删除对应的记录
    db.session.commit()  # 提交数据库会话
    flash('Item deleted.')
    return redirect(url_for('index_database'))  # 重定向回主页




from flask_login import login_required, current_user
# ...
#山大成绩单的设定用户视图
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
        return redirect(url_for('index_database'))

    return render_template('settings.html')


from flask_login import login_user
# ...
#山大成绩单的登入视图
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
# 山大成绩单的登出视图
@app.route('/logout')
@login_required  # 用于视图保护，后面会详细介绍
def logout():
    logout_user()  # 登出用户
    flash('Goodbye.')
    return redirect(url_for('index_database'))  # 重定向回首页




#国科大成绩单的主视图
@app.route('/ucas', methods=['GET', 'POST'])
def index_database_ucas():
    if request.method == 'POST':  # 判断是否是 POST 请求
        if not current_user.is_authenticated:  # 如果当前用户未认证
            return redirect(url_for('index_database'))  # 重定向到主页
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
        course = Transcripts_ucas(title=title, year=year, Grade=Grade, Hours=Hours, Credits=Credits)  # 创建记录
        db.session.add(course)  # 添加到数据库会话
        db.session.commit()  # 提交数据库会话
        flash('Item created.')  # 显示成功创建的提示
        return redirect(url_for('index_database'))  # 重定向回主页

    courses = Transcripts_ucas.query.all()  # 读取所有电影记录
    return render_template('index_database_ucas.html', Transcripts=courses)


#国科大成绩单的主视图
@app.route('/cityuhk', methods=['GET', 'POST'])
def index_database_cityuhk():
    if request.method == 'POST':  # 判断是否是 POST 请求
        if not current_user.is_authenticated:  # 如果当前用户未认证
            return redirect(url_for('index_database'))  # 重定向到主页
        # 获取表单数据
        title = request.form.get('title')  # 传入表单对应输入字段的 name 值
        year = request.form.get('year')
        Credits = request.form.get('Credits')
        Code = request.form.get('Code')
        Grade = request.form.get('Grade')
        # 验证数据
        if not title or not year or len(year) > 10 or len(title) > 60:
            flash('Invalid input.')  # 显示错误提示
            return redirect(url_for('index_database'))  # 重定向回主页
        # 保存表单数据到数据库
        course = Transcripts_cityuhk(title=title, year=year, Grade=Grade, Code=Code, Credits=Credits)  # 创建记录
        db.session.add(course)  # 添加到数据库会话
        db.session.commit()  # 提交数据库会话
        flash('Item created.')  # 显示成功创建的提示
        return redirect(url_for('index_database'))  # 重定向回主页

    courses = Transcripts_cityuhk.query.all()  # 读取所有电影记录
    return render_template('index_database_cityuhk.html', Transcripts=courses)


#国科大成绩单的主视图
@app.route('/polyuhk', methods=['GET', 'POST'])
def index_database_polyuhk():
    if request.method == 'POST':  # 判断是否是 POST 请求
        if not current_user.is_authenticated:  # 如果当前用户未认证
            return redirect(url_for('index_database'))  # 重定向到主页
        # 获取表单数据
        title = request.form.get('title')  # 传入表单对应输入字段的 name 值
        year = request.form.get('year')
        Credits = request.form.get('Credits')
        Code = request.form.get('Code')
        Grade = request.form.get('Grade')
        # 验证数据
        if not title or not year or len(year) > 10 or len(title) > 60:
            flash('Invalid input.')  # 显示错误提示
            return redirect(url_for('index_database'))  # 重定向回主页
        # 保存表单数据到数据库
        course = Transcripts_polyuhk(title=title, year=year, Grade=Grade, Code=Code, Credits=Credits)  # 创建记录
        db.session.add(course)  # 添加到数据库会话
        db.session.commit()  # 提交数据库会话
        flash('Item created.')  # 显示成功创建的提示
        return redirect(url_for('index_database_polyuhk'))  # 重定向回主页

    courses = Transcripts_polyuhk.query.all()  # 读取所有电影记录
    return render_template('index_database_polyuhk.html', Transcripts=courses)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')