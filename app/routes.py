import json
from flask import Flask, render_template, url_for, redirect, flash, request, json
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bootstrap import Bootstrap
from app import app, db
from app.models import User, Transaction
from app.forms import LoginForm, RegisterForm, MaxBudgetForm, AddForm
from werkzeug.urls import url_parse

# app.debug = True
@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/deleteAccount')
@login_required
def delete_account():
    user = User.query.filter_by(id=current_user.id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/TransactionHistory')
@login_required
def transaction_history():
    return render_template('TransactionHistory.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        # Check if signin info was correct
        if user is None or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for("signin"))
        
        # Successful signin
        login_user(user, remember=form.remember.data)
        
        # Return user to previous page if redirected here,
        # or to user's transaction history page if visited directly
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('transaction_history')
        
        return redirect(next_page)

    return render_template('signin.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # already registerd users cannot register again
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        # store the hash of the user's password
        new_user.set_password(form.password.data)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('You are now a registered user!')
        return redirect(url_for('signin'))

    return render_template('signup.html', form=form)


@app.route('/AddTrans', methods = ['GET', 'POST'])
@login_required
def add_trans():
    form = AddForm()
    user = User.query.filter_by(id=current_user.id).first()
    
    if form.validate_on_submit():
        t = Transaction(amount = form.amount.data, description =  form.description.data, author = user)

        db.session.add(t)
        db.session.commit()
        flash(t)
    return render_template('AddTrans.html', form = form)


@app.route('/TransactionStats', methods=['GET', 'POST'])
@login_required
def transaction_stats():

    form = MaxBudgetForm()
    user = User.query.filter_by(id=current_user.id).first()
    budget = user.max_budget
    transactions = Transaction.query.filter_by(user_id=current_user.id)

    # data for the chart
    amounts = []
    labels = []
    descriptions = []
    for t in transactions:
        labels.append(t.timestamp)
        descriptions.append(t.description)
        sum = 0
        for x in range(1, len(amounts)):
            sum = sum + transactions[x-1].amount
        amounts.append(sum)

    def is_jsonable(x):
        try: 
            json.dumps(x)
        except:
            return render_template('TransactionStats.html', noData=True)


    is_jsonable(transactions)
    is_jsonable(budget)
    is_jsonable(amounts)
    is_jsonable(descriptions)
    is_jsonable(labels)
    try: 
        is_jsonable(amounts[0])
    except:
        flash('no data')
        return render_template('TransactionStats.html', noData=True)

    if form.validate_on_submit():
        user.set_max_budget(form.max_budget.data)
        db.session.commit()
        return redirect(url_for('transaction_stats'))

    return render_template('TransactionStats.html', noData=False, data=transactions, amts=amounts, lbls=labels, budget=budget, desc=descriptions, form=form)
