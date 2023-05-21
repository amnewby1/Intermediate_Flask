from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Feedback
from forms import RegisterForm, LoginForm, FeedbackForm
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///user_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)

toolbar = DebugToolbarExtension(app)

db.create_all()

@app.route('/')
def redirect_to_register():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email=form.email.data
        first_name=form.first_name.data
        last_name=form.last_name.data
        new_user = User.register(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append('Username taken.  Please pick another')
            return render_template('register.html', form=form)
        session['username'] = new_user.username
        flash('Welcome! Successfully Created Your Account!', "success")
        return redirect(f'/users/{new_user.username}')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome Back, {user.username}!", "primary")
            session['username'] = user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_user():
    session.pop('username')
    flash("Goodbye!", "info")
    return redirect('/')

@app.route('/users/<username>')
def show_secret(username):
    user=User.query.get(username)

    if "username" not in session or username != session["username"]:
        flash("Please login first!", "danger")
        return redirect('/login')
    
    feedbacks=Feedback.query.all()
    
    return render_template("user_info.html", user=user, feedbacks=feedbacks)

@app.route('/users/<username>/delete', methods=["POST"])
def delete_user(username):
    if "username" not in session or username != session['username']:
        flash("Please login first!", "danger")
        return redirect('/login')
    user = User.query.get_or_404(username)
    if user.username == session['username']:
        db.session.delete(user)
        db.session.commit()
        flash("User deleted!", "success")
        return redirect('/login')
    flash("You don't have permission to do that!", "danger")
    return redirect('/login')

@app.route('/users/<username>/feedback/add', methods=['GET', 'POST'])
def add_feedback(username):
    if "username" not in session or username != session['username']:
        flash("Please login first!", "danger")
        return redirect('/login')
    user=User.query.get_or_404(username)
    form=FeedbackForm()

    if form.validate_on_submit():
        title= form.title.data
        content = form.content.data
        username=session['username']
        new_feedback = Feedback(title=title, content=content, username=username)

        db.session.add(new_feedback)
        db.session.commit()
        return redirect(f'/users/{new_feedback.username}')
    return render_template('add_feedback.html', user=user, form=form)

@app.route('/feedback/<int:feedback_id>/update', methods=["GET", "POST"])
def edit_feedback(feedback_id):
    feedback=Feedback.query.get(feedback_id)
    if "username" not in session or feedback.username != session['username']:
        flash("Please login first", "danger")
        return redirect('/login')
    
    form=FeedbackForm(obj=feedback)

    if form.validate_on_submit():
        feedback.title=form.title.data
        feedback.content=form.content.data
        db.session.commit()
        return redirect (f'/users/{feedback.username}')
    else:
        return render_template("edit_feedback.html",form=form, feedback=feedback)

@app.route('/feedback/<int:feedback_id>/delete', methods=['GET','POST'])
def delete_feedback(feedback_id):
    feedback=Feedback.query.get(feedback_id)
    if "username" not in session or feedback.username != session['username']:
        flash("Please login first", "danger")
        return redirect('/login')
        user = User.query.get_or_404(username)
    if feedback.username == session['username']:
        db.session.delete(feedback)
        db.session.commit()
        flash("Feedback deleted!", "success")
        
    return redirect(f'/users/{feedback.username}')
   