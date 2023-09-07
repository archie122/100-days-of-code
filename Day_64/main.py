from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# CONFIGUR LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()

logged_in = False

@app.route('/')
def home():
    return render_template("index.html", logged_in=logged_in)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if len(request.form['password']) < 6:
            error = "Password must be at least 6 characters"
        elif db.session.execute(db.select(User).where(User.email == request.form['email'])):
            error = "Email already exists"
        else:
            new_user = User(
                name=request.form['name'],
                email=request.form['email'],
                password=generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
            )

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            global logged_in
            logged_in = True
            return render_template("secrets.html", name=new_user.name, logged_in=logged_in)
    return render_template("register.html", error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Welcome, {}'.format(user.name), category='success')
                global logged_in
                logged_in = True
                return render_template("secrets.html", name=user.name, logged_in=logged_in)
            else:
                error = 'Password is incorrect'
        else:
            error = 'Email does not exist, try again.'

    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    logout_user()
    global logged_in
    logged_in = False
    return render_template("index.html", logged_in=logged_in)


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
