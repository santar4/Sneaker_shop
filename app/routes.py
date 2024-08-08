from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, User, db, models
from app.forms import SignUpForm, LoginForm


@app.route("/")
def index():

    return render_template("index.html", )


@app.route('/male')
def male():
    all_shoes = db.session.execute(db.select(models.Sneaker).filter_by(models.Sneaker.gender == "male")).scalars()
    return render_template("all_shoes_for_gender.html", all_ah=all_shoes)


@app.route('/female')
def female():
    all_shoes = db.session.execute(db.select(models.Sneaker).filter_by(models.Sneaker.gender == "female")).scalars()
    return render_template("all_shoes_for_gender.html", all_ah=all_shoes)


# @app.route('/search', methods=['GET'])
# def search():
#     query = request.args.get('q')  # Получаем поисковый запрос
#     results = get_products(query)  # Выполняем поиск по базе данных
#     return render_template('search_results.html', results=results)




@app.route('/details/<int:id_shoes>')
def details_shooze(id_shoes):
    data_shoes = ...# db.get_or_404(models.Sneaker, id_shoes)
    return render_template("details_shoes.html",
                           data = data_shoes)

    return


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


@app.route("/user/login/", methods=["GET", "POST"])
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
