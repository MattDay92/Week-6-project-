from app import app
from flask import render_template, request, redirect, url_for
from .forms import UserCreationForm, loginform, ItemSubmitForm
from .models import User, Item
from flask_login import login_user, logout_user, current_user



@app.route('/')
def home():
    return render_template('index.html')






@app.route('/signup', methods=["GET", "POST"])
def signUpPage():
    form = UserCreationForm()
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            
            print(username, email, password)

            # add user to database
            user = User(username, email, password)
            # print(user)

            user.saveToDB()

            return redirect(url_for('home'))


    return render_template('signup.html', form = form )



@app.route('/login' , methods=['GET','POST' ])
def loginPage():
    form = loginform()
    if request.method == 'POST':
        if form.validate():
            username= form.username.data
            password = form.password.data

            #check is user with that username
            user = User.query.filter_by(username=username).first()
            # print(user)
            if user:

                if user.passwrod == password:
                
                    login_user(user)
                    

                else:
                    print("Wrong password")
            else:
                print("This user does not exist.")



    return render_template('login.html' , form = form)
 


@app.route('/logout', methods=['GET'])
def logout():
    logout_user
    return redirect(url_for('loginPage'))





@app.route('/admin', methods=['GET', 'POST'])
def adminPage():
    form = ItemSubmitForm()
    print(request.method)
    if request.method == 'POST':
        if form.validate():
            name = form.name.data
            img_url = form.img_url.data
            details = form.details.data

            item = Item(name, img_url, details)

            item.saveToDB()

            return redirect(url_for('adminPage'))

    return render_template('admin.html', form=form)

