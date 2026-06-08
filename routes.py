from flask import render_template, redirect, flash, request, abort
from ext import app, db
from forms import RegisterForm, LoginForm, ChampionshipForm
from models import User, Championship
from flask_login import login_user, logout_user, login_required, current_user
from os import path


@app.route("/")
def home():
    championships = Championship.query.all()
    return render_template("index.html", championships=championships)


@app.route("/championship/<int:championship_id>")
def championship_details(championship_id):
    c = Championship.query.get_or_404(championship_id)
    return render_template("details.html", c=c)


@app.route("/add_championship", methods=["GET", "POST"])
@login_required
def add_championship():
    if current_user.role != "Admin":
        return abort(403)

    form = ChampionshipForm()
    if form.validate_on_submit():
        new_c = Championship(
            title=form.title.data,
            sport=form.sport.data,
            year=form.year.data,
            winner=form.winner.data,
            runner_up=form.runner_up.data,
            team1=form.team1.data,
            team2=form.team2.data,
            final_score=form.final_score.data,
            semi_final_1=form.semi_final_1.data,
            semi_final_2=form.semi_final_2.data,
            description=form.description.data,
            img="default_image.jpg"
        )

        file = form.image.data
        if file and file.filename != '':
            file_directory = path.join(app.root_path, "static", "images", file.filename)
            file.save(file_directory)
            new_c.img = file.filename

        new_c.create()
        flash("Successfully created a new tournament card!")
        return redirect("/")

    return render_template("add_championship.html", form=form, heading="Add Championship")


@app.route("/update_championship/<int:championship_id>", methods=["GET", "POST"])
@login_required
def update_championship(championship_id):
    if current_user.role != "Admin":
        return abort(403)

    c = Championship.query.get_or_404(championship_id)
    form = ChampionshipForm(
        title=c.title, sport=c.sport, year=c.year, winner=c.winner,
        runner_up=c.runner_up, team1=c.team1, team2=c.team2,
        final_score=c.final_score, semi_final_1=c.semi_final_1,
        semi_final_2=c.semi_final_2, description=c.description
    )

    if form.validate_on_submit():
        c.title = form.title.data
        c.sport = form.sport.data
        c.year = form.year.data
        c.winner = form.winner.data
        c.runner_up = form.runner_up.data
        c.team1 = form.team1.data
        c.team2 = form.team2.data
        c.final_score = form.final_score.data
        c.semi_final_1 = form.semi_final_1.data
        c.semi_final_2 = form.semi_final_2.data
        c.description = form.description.data

        file = form.image.data
        if file and file.filename != '':
            file_directory = path.join(app.root_path, "static", "images", file.filename)
            file.save(file_directory)
            c.img = file.filename

        c.save()
        flash("Tournament data updated successfully!")
        return redirect(f"/championship/{c.id}")

    return render_template("add_championship.html", form=form, heading="Modify Championship")


@app.route("/delete_championship/<int:championship_id>")
@login_required
def delete_championship(championship_id):
    if current_user.role != "Admin":
        return abort(403)

    c = Championship.query.get_or_404(championship_id)
    c.delete()
    flash("Tournament card removed completely.")
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)
        new_user.create()
        flash("Account created!")
        return redirect("/login")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        flash("Invalid username or password")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")