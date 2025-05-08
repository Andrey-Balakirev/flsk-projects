from flask import Flask, render_template
from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city
from webapp.model import db
from datetime import datetime
from webapp.model import db, News, User
from webapp.python_org_news import save_news
from webapp.python_org_news import get_html
from webapp.forms import LoginForm
from flask_login import LoginManager
from flask_login import LoginManager, login_user
from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required,login_user, logout_user


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    

    @app.route('/')
    def index():
        title = "Новости Python"
        city = app.config["WEATHER_DEFAULT_CITY"]
        weather = weather_by_city(city_name= city)
        data = get_html(url = "https://www.python.org/blogs/")
        news = get_python_news(data)
       # save_news(title="новости погоды",url="https://sqlitebrowser.org/dl/2",published=datetime(2025,4,17,18,56,54))
        return render_template('index.html', page_title=title,
        weather=weather, news_list= news)
    
    
    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)
        

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы вошли на сайт')
                return redirect(url_for('index'))
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
           return 'Привет админ'
        else:
           return 'Ты не админ!'
        
    
    return app