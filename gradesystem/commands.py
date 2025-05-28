import click

from gradesystem import app, db
from gradesystem.models import User, Transcripts, Transcripts_ucas, Transcripts_cityuhk, Transcripts_polyuhk

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
        {'title': 'College Comprehensive English (1)',              'year': '2016 I',  'Grade': '83.4','Hours':'120','Credits':'4.0'},
        {'title': 'Advanced Mathematics I (1)',                     'year': '2016 I',   'Grade': '92',  'Hours':'80',   'Credits':'5.0'},
        {'title': 'Mechanics',                                      'year': '2016 I',   'Grade': '98',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Fundamental Physics Experiments (1)',            'year': '2016 I',   'Grade': '87',  'Hours':'48',   'Credits':'1.5'},
        {'title': 'Introduction of Computer (C++ Programming)',     'year': '2016 I',   'Grade': '91','Hours':'64','Credits':'3.0'},
        {'title': 'Morals and Law',                                 'year': '2016 I',   'Grade': '87','Hours':'58','Credits':'3.0'},
        {'title': 'Physical Education (1)',                         'year': '2016 I',   'Grade': '72','Hours':'32','Credits':'1.0'},
        {'title': 'Martial Training',                               'year': '2016 I',   'Grade': 'qualified','Hours':'2 Weeks','Credits':'0.0'},
        {'title': 'College Comprehensive English (2)',              'year': '2016 II',  'Grade': '83.5','Hours':'120','Credits':'4.0'},
        {'title': 'Advanced Mathematics I (2)',                     'year': '2016 II',   'Grade': '97','Hours':'80','Credits':'5.0'},
        {'title': 'Thermal Physics',                                'year': '2016 II',   'Grade': '92',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Electromagnetics',                               'year': '2016 II',   'Grade': '97.6',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Fundamental Physics Experiments (2)',            'year': '2016 II',   'Grade': '88',  'Hours':'64',   'Credits':'2.0'},
        {'title': 'Brief of Chinas Modern History',                 'year': '2016 II',   'Grade': '90',  'Hours':'29',   'Credits':'1.5'},
        {'title': 'Trend, Policy and Social Practice (1-2)',        'year': '2016 II',   'Grade': '85.1',  'Hours':'12',   'Credits':'0.5'},
        {'title': 'Physical Education (2)',                         'year': '2016 II',   'Grade': '74',  'Hours':'32',   'Credits':'1.0'},
        {'title': 'Military Theory',                                'year': '2016 II',   'Grade': '91',  'Hours':'32',   'Credits':'2.0'},
        {'title': 'Chinese and Western Culture',                    'year': '2016 II',   'Grade': 'qualified',  'Hours':'32',   'Credits':'2.0'},
        {'title': 'Collegiate Programming Contest',                 'year': '2016 II',   'Grade': 'qualified',  'Hours':'32',   'Credits':'2.0'},
        {'title': 'New Conspectus of Astronomy',                    'year': '2016 II',   'Grade': 'excellent',  'Hours':'16',   'Credits':'1.0'},
        {'title': 'Amateur Astronomical Observation & Photography', 'year': '2016 II',   'Grade': 'excellent',  'Hours':'24',   'Credits':'1.0'},
        {'title': 'Introduction to Space Science',                  'year': '2016 III',   'Grade': '81',  'Hours':'16',   'Credits':'1.0'},
        {'title': 'Psychological Movie Appreciation',               'year': '2016 III',   'Grade': 'qualified',  'Hours':'16',   'Credits':'1.0'},
        {'title': 'Linear Algebra II',                              'year': '2017 I',   'Grade': '93',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Optics',                                         'year': '2017 I',   'Grade': '96',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Fundamental Physics Experiments (3)',            'year': '2017 I',   'Grade': '88',  'Hours':'48',   'Credits':'1.5'},
        {'title': 'Methods of Mathematical Physics',                'year': '2017 I',   'Grade': '98',  'Hours':'64',   'Credits':'4.0'},
        {'title': 'Theoretical Mechanics',                          'year': '2017 I',   'Grade': '89',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Fundamental Astronomy',                          'year': '2017 I',   'Grade': '89',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Chinese Marxism',                                'year': '2017 I',   'Grade': '79',  'Hours':'58',   'Credits':'3.0'},
        {'title': 'Physical Education (3)',                         'year': '2017 I',   'Grade': '83',  'Hours':'32',   'Credits':'1.0'},
        {'title': 'Introduction to Earth Science',                             'year': '2017 I',   'Grade': '92',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'History of Chinese Aesthetical Culture',                    'year': '2017 I',   'Grade': 'qualified',  'Hours':'32',   'Credits':'2.0'},
        {'title': 'Comment and Appreciation of Modern Poetry',                 'year': '2017 I',   'Grade': 'qualified',  'Hours':'32',   'Credits':'2.0'},
        {'title': 'History of Qin and Han Dynasties',                          'year': '2017 I',   'Grade': '85',  'Hours':'22',   'Credits':'1.0'},
        {'title': 'Probability and Mathematical Statistics II',                'year': '2017 II',   'Grade': '90',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Atomic Physics',                                            'year': '2017 II',   'Grade': '97',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Electrodynamics',                                           'year': '2017 II',   'Grade': '93',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Quantum Mechanics',                                         'year': '2017 II',   'Grade': '93',  'Hours':'64',   'Credits':'4.0'},
        {'title': 'Basic Principles of Marxism',                               'year': '2017 II',   'Grade': '84',  'Hours':'58',   'Credits':'3.0'},
        {'title': 'Trend, Policy and Social Practice (3-4)',                   'year': '2017 II',   'Grade': '91',  'Hours':'12',   'Credits':'0.5'},
        {'title': 'Physical Education (4)',                                    'year': '2017 II',   'Grade': '69',  'Hours':'32',   'Credits':'1.0'},
        {'title': 'Surveying & Engineering Surveying',                         'year': '2017 II',   'Grade': '91',  'Hours':'56',   'Credits':'3.0'},
        {'title': 'Fluid Mechanics',                                           'year': '2017 II',   'Grade': '93',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Introduction to Planetary Science',                         'year': '2017 II',   'Grade': '92',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'History of Sui and Tang Dynastics',                         'year': '2017 II',   'Grade': '93',  'Hours':'22',   'Credits':'1.0'},
        {'title': 'Innovation Experiments of Physics',                         'year': '2017 III',   'Grade': '92',  'Hours':'16',   'Credits':'0.5'},
        {'title': 'Advances in Space Physics',                                 'year': '2017 III',   'Grade': '92',  'Hours':'16',   'Credits':'1.0'},
        {'title': 'Advances in Planetary Science',                             'year': '2017 III',   'Grade': '83',  'Hours':'16',   'Credits':'1.0'},
        {'title': 'The Progress of Satellite Navigation and Remote Sensing',   'year': '2017 III',   'Grade': '93',  'Hours':'16',   'Credits':'1.0'},
        {'title': 'Thermodynamics and Statistic Physics',                      'year': '2018 I',   'Grade': '89.3',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Modern Physics Experiments (1)',                            'year': '2018 I',   'Grade': '84',  'Hours':'48',   'Credits':'1.5'},
        {'title': 'Crystallography and Mineralogy',                            'year': '2018 I',   'Grade': '86.9',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Surveying Adjustment',                                      'year': '2018 I',   'Grade': '98',  'Hours':'40',   'Credits':'2.5'},
        {'title': 'Photogrammetry & Remote Sensing',                           'year': '2018 I',   'Grade': '93.2',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Space Observations and Instrumentations',                   'year': '2018 I',   'Grade': '81',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Planetary Spectroscopy and Remote Sensing',                 'year': '2018 I',   'Grade': '81',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Modern Physics Experiments (2)',                            'year': '2018 II',   'Grade': '85',  'Hours':'48',   'Credits':'1.5'},
        {'title': 'Computational Physics and Experiment',                      'year': '2018 II',   'Grade': '92',  'Hours':'64',   'Credits':'3.0'},
        {'title': 'Trend, Policy and Social Practice (5-6)',                   'year': '2018 II',   'Grade': '89',  'Hours':'12',   'Credits':'0.5'},
        {'title': 'Lab Space Physics',                                         'year': '2018 II',   'Grade': '84',  'Hours':'32',   'Credits':'1.0'},
        {'title': 'Geodesy',                                                   'year': '2018 II',   'Grade': '80',  'Hours':'40',   'Credits':'2.5'},
        {'title': 'Foundation of Satellite Navigation',                        'year': '2018 II',   'Grade': '87',  'Hours':'56',   'Credits':'3.0'},
        {'title': 'Introduction to Plasma Physics',                            'year': '2018 II',   'Grade': '84',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Introduction to Space Physics',                             'year': '2018 II',   'Grade': '86',  'Hours':'48',   'Credits':'3.0'},
        {'title': 'Planetary Materials',                                       'year': '2018 II',   'Grade': '87.5',  'Hours':'48',   'Credits':'2.5'},
        {'title': 'Computer Network',                                          'year': '2018 II',   'Grade': 'qualified',  'Hours':'32',   'Credits':'2.0'},
        {'title': 'Principle of Computer Organization',                        'year': '2018 II',   'Grade': '87',  'Hours':'80',   'Credits':'4.5'},
        {'title': 'Practice in Space Science',                                 'year': '2018 III',   'Grade': '83',  'Hours':'1 weeks',   'Credits':'1.0'},
        {'title': 'Data Structure',                                            'year': '2019 I',   'Grade': '88',  'Hours':'80',   'Credits':'4.5'},
        {'title': 'Database Systems',                                          'year': '2019 I',   'Grade': '91',  'Hours':'80',   'Credits':'4.5'},
        {'title': 'Operating Systems',                                         'year': '2019 I',   'Grade': '86',  'Hours':'64',   'Credits':'4.0'},
        {'title': 'Java Programming',                                          'year': '2019 I',   'Grade': '99',  'Hours':'64',   'Credits':'3.5'},
        {'title': 'Introduction of Artificial Intelligence',                   'year': '2019 I',   'Grade': '91',  'Hours':'32',   'Credits':'2.0'},
        {'title': 'Senior Thesis',                                             'year': '2019 II',   'Grade': '89',  'Hours':'12 weeks',   'Credits':'8.0'},
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
        user = User(username=username, name='LIU Baoshan')
        user.set_password(password)  # 设置密码
        db.session.add(user)

    db.session.commit()  # 提交数据库会话
    click.echo('Done.')





# 添加命令行命令：写入数据
@app.cli.command()
def forge_ucas():
    """写入成绩数据到数据库"""
    db.create_all()  # 确保表存在

    name = 'LIU Baoshan'
    Transcripts_data = [
        {'title': 'The Study of Theory and Practice of Socialism with Chinese Characteristics',              'year': '2020 I',  'Grade': '82','Hours':'36','Credits':'2.0'},
        {'title': 'MS English Program',                                     'year': '2020 I',   'Grade': '75',  'Hours':'64',   'Credits':'3.0'},
        {'title': 'History of Science and Technology',                      'year': '2020 I',   'Grade': '90',  'Hours':'40',   'Credits':'1.0'},
        {'title': 'Stochastic Processes',                                   'year': '2020 I',   'Grade': '87',  'Hours':'60',   'Credits':'4.0'},
        {'title': 'Optimization Methods in Algorithm',                      'year': '2020 I',   'Grade': '87',  'Hours':'40',   'Credits':'2.0'},
        {'title': 'Advanced Artificial Intelligence',                       'year': '2020 I',   'Grade': '92',  'Hours':'60',   'Credits':'3.0'},
        {'title': 'Pattern Recognition and Machine Learning',               'year': '2020 I',   'Grade': '81',  'Hours':'60',   'Credits':'3.0'},
        {'title': 'Advanced Digital Signal Processing',                     'year': '2020 I',   'Grade': '82',  'Hours':'40',   'Credits':'2.0'},
        {'title': 'The Design and Analysis of Computer Algorithm',          'year': '2020 I',   'Grade': '86',  'Hours':'60',   'Credits':'3.0'},
        {'title': 'Academic Ethics and Writing Norms',                      'year': '2020 I',   'Grade': '90',  'Hours':'20',   'Credits':'1.0'},
        {'title': 'Introduction to Dialectics of Nature',                   'year': '2020 II',   'Grade': '91',  'Hours':'36',   'Credits':'1.0'},
        {'title': 'Japanese',                                               'year': '2020 II',   'Grade': '98',  'Hours':'64',   'Credits':'2.0'},
        {'title': 'Matrix Analysis and Application',                        'year': '2020 II',   'Grade': '82',  'Hours':'60',   'Credits':'4.0'},
        {'title': 'Robot Visual Localization and Navigation',               'year': '2020 II',   'Grade': '95',  'Hours':'20',   'Credits':'1.0'},
        {'title': 'Image Processing and Computer Vision',                   'year': '2020 II',   'Grade': '89',  'Hours':'40',   'Credits':'2.0'},
        {'title': 'Principles of GNSS Positioning and its Applications',    'year': '2020 II',   'Grade': '79',  'Hours':'30',   'Credits':'2.0'},
        {'title': 'Big Data System and Large-Scale Data Analysis',          'year': '2020 II',   'Grade': '84',  'Hours':'50',   'Credits':'3.0'},
        {'title': 'Database New Technology',                                'year': '2020 II',   'Grade': '93',  'Hours':'40',   'Credits':'2.0'},
        {'title': 'International Trade',                                    'year': '2020 III',   'Grade': '94',  'Hours':'20',   'Credits':'1.0'},
        {'title': 'Optimization and Simulation Methods in Finance',         'year': '2020 III',   'Grade': '97',  'Hours':'20',   'Credits':'1.0'},
        {'title': 'Frontier of Sciences I',                                 'year': '2020 III',   'Grade': 'Pass',  'Hours':'20',   'Credits':'1.0'},
    ]

    # 添加用户
    user = User(name=name)
    db.session.add(user)

    # 添加所有课程
    for item in Transcripts_data:
        transcript = Transcripts_ucas(
            title=item['title'],
            year=item['year'],
            Grade=item['Grade'],
            Hours=item['Hours'],
            Credits=item['Credits']
        )
        db.session.add(transcript)

    db.session.commit()
    click.echo('UCAS成绩数据已成功写入数据库！')






# 添加命令行命令：写入数据
@app.cli.command()
def forge_cityuhk():
    """写入成绩数据到数据库"""
    db.create_all()  # 确保表存在

    name = 'LIU Baoshan'
    Transcripts_data = [
        {'title': 'Machine Learning for Signal Processing Application',                 'year': '2023 I',  'Grade': 'A-','Code':'EE5434','Credits':'3.0'},
        {'title': 'Applied Deep Learning',                                              'year': '2023 I',   'Grade': 'A-',  'Code':'EE5438',   'Credits':'3.0'},
        {'title': 'Topics in Security Technology',                                      'year': '2023 I',   'Grade': 'B+',  'Code':'EE5815',   'Credits':'3.0'},
        {'title': 'Complex Networks: Modeling, Dynamics and Control',                   'year': '2023 I',   'Grade': 'A',  'Code':'EE6605',   'Credits':'3.0'},
        {'title': 'Detection and Estimation - Theory and Application in Communications','year': '2023 I',   'Grade': 'A-',  'Code':'EE6617',   'Credits':'3.0'},
        {'title': 'Telecommunication Networks',                                         'year': '2023 II',   'Grade': 'A-',  'Code':'EE5412',   'Credits':'3.0'},
        {'title': 'Internet of Things Technologies for Future City Applications',       'year': '2023 II',   'Grade': 'B+',  'Code':'EE5437',   'Credits':'3.0'},
        {'title': 'Multi-Dimensional Data Modeling and its Applications',               'year': '2023 II',   'Grade': 'A-',  'Code':'EE6435',   'Credits':'3.0'},
        {'title': 'Queueing Theory with Telecommunications Applications',               'year': '2023 II',   'Grade': 'A-',  'Code':'EE6610',   'Credits':'3.0'},
        {'title': 'Linear Systems Theory and Design',                                   'year': '2023 II',   'Grade': 'A-',  'Code':'EE6620',   'Credits':'3.0'},
    ]

    # 添加用户
    user = User(name=name)
    db.session.add(user)

    # 添加所有课程
    for item in Transcripts_data:
        transcript = Transcripts_cityuhk(
            title=item['title'],
            year=item['year'],
            Grade=item['Grade'],
            Code=item['Code'],
            Credits=item['Credits']
        )
        db.session.add(transcript)

    db.session.commit()
    click.echo('CityUHK成绩数据已成功写入数据库！')



# 添加命令行命令：写入数据
@app.cli.command()
def forge_polyuhk():
    """写入成绩数据到数据库"""
    db.create_all()  # 确保表存在

    name = 'LIU Baoshan'
    Transcripts_data = [
        {'title': 'Engineering Integrity and Academic Integrity',                   'year': '2025 I',   'Grade': 'unknown',  'Code':'EEE5R03',   'Credits':'1.0'},
        {'title': 'Methodology for Engineering and Scientific Research',            'year': '2025 I',   'Grade': 'unknown',  'Code':'EEE6200',   'Credits':'3.0'},
        {'title': 'Research Seminar I',                                             'year': '2025 I',   'Grade': 'unknown',  'Code':'EEE6201',   'Credits':'1.0'},
        {'title': 'Research Seminar II',                                            'year': '2025 I',   'Grade': 'unknown',  'Code':'EEE6202',   'Credits':'1.0'},
        {'title': 'Research Seminar III',                                           'year': '2025 I',   'Grade': 'unknown',  'Code':'EEE6203',   'Credits':'1.0'},
        {'title': 'Practicum',                                                      'year': '2025 I',   'Grade': 'unknown',  'Code':'EEE6002',   'Credits':'2.0'},
        {'title': 'Presentation Skills for Research Students',                      'year': '2025 I',   'Grade': 'unknown',  'Code':'ELC6011',   'Credits':'2.0'},
        {'title': 'Thesis Writing for Research Students',                           'year': '2025 I',   'Grade': 'unknown',  'Code':'ELC6012',   'Credits':'3.0'},
        {'title': 'Advanced Theory and Methods in Vibration Analysis',              'year': '2025 I',   'Grade': 'unknown',  'Code':'ME6101',   'Credits':'3.0'},
        {'title': 'Advanced Topics in Control, Acoustics, and Dynamics',            'year': '2025 I',   'Grade': 'unknown',  'Code':'ME6102',   'Credits':'3.0'},
        {'title': 'Theoretical Fundamental and Engineering Approaches for Intelligent Signal and Information Processing',              'year': '2025 I',   'Grade': 'unknown',  'Code':'EEE6207',   'Credits':'3.0'},
        {'title': 'Advanced Statistical Learning',                                   'year': '2025 I',   'Grade': 'unknown',  'Code':'AMA620',   'Credits':'3.0'},
    ]

    # 添加用户
    user = User(name=name)
    db.session.add(user)

    # 添加所有课程
    for item in Transcripts_data:
        transcript = Transcripts_polyuhk(
            title=item['title'],
            year=item['year'],
            Grade=item['Grade'],
            Code=item['Code'],
            Credits=item['Credits']
        )
        db.session.add(transcript)

    db.session.commit()
    click.echo('PolyUHK成绩数据已成功写入数据库！')