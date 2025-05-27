import click

from gradesystem import app, db
from gradesystem.models import User, Transcripts

@app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息




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


