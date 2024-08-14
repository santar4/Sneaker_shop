import os
from io import BytesIO

from flask import render_template, flash, redirect, url_for, request, send_file
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from app import app, User, db,  models
from app.models import Sneaker
from app.forms import SignUpForm, LoginForm

@app.route("/")
def index():
    return  render_template("index.html")

@app.route('/add-sneaker', methods=['GET', 'POST'])
def add_sneaker():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        prize = int(request.form['prize'])
        gender = request.form['gender']
        image_file = request.files['image']

        if image_file:
            filename = secure_filename(image_file.filename)
            upload_folder = app.config['UPLOAD_FOLDER']

            image_path = os.path.join(upload_folder, filename)

            if os.path.exists(image_path):
                flash('File already exists. Please choose a different file.', 'danger')
                return redirect(url_for('add_sneaker'))

            try:
                image_file.save(image_path)
            except Exception as e:
                flash(f'An error occurred while saving the file: {str(e)}', 'danger')
                return redirect(url_for('add_sneaker'))

            with open(image_path, 'rb') as f:
                image_data = f.read()


            new_sneaker = Sneaker(name=name, description=description, prize=prize, gender=gender, image=image_data)
            db.session.add(new_sneaker)
            db.session.commit()


            os.remove(image_path)

            flash('Sneaker added successfully!', 'success')
            return redirect(url_for('add_sneaker'))

    return render_template('add_sneaker.html')


@app.route('/male')
def male():
    all_shoes = db.session.execute(
        db.select(models.Sneaker).filter(models.Sneaker.gender == "Male")
    ).scalars().all()
    return render_template("all_shoes_.html", all_sh=all_shoes)



@app.route('/female')
def female():
    all_shoes = db.session.execute(
        db.select(models.Sneaker).filter(models.Sneaker.gender == "Female")
    ).scalars().all()
    return render_template("all_shoes_.html", all_sh=all_shoes)




@app.route('/details/<int:id_shoes>')
def details_shoes(id_shoes):
    data_shoes = db.get_or_404(models.Sneaker, id_shoes)
    return render_template("details_shoes.html",
                           sneaker=data_shoes)

@app.route("/signup/", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if user:
            flash("User currently exists")
            return redirect(url_for("login"))
        new_user = User(
            nickname=form.nickname.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("user/signup.html", form=form, title="Signup")

@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.query(User).where(User.nickname == form.nickname.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        else:
            flash("Invalid nickname or password")

    return render_template("user/login.html", form=form, title="Login")


@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))