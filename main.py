from flask import Flask, request, redirect, render_template
import cgi

app=Flask(__name__)

app.config['DEBUG'] = True

user_name=""

@app.route("/add-account", methods=['POST'])
def add_account():
    user_name = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']
    if user_name == "":
        return redirect("/username-error")
    if len(user_name)<3 or len(user_name)>20:
        return redirect("/username-error")
    if password == "":
        return redirect("/password-error?user_name={0}&email={1}".format(user_name, email))
    if len(password)<3 or len(password)>20:
        return redirect("/password-error?user_name={0}&email={1}".format(user_name, email))
    if password != verify_password:
        return redirect("/verify-password-error?user_name={0}&email={1}".format(user_name, email))
    if " " in email:
        return redirect("/email-error?user_name={0}&email={1}".format(user_name, email))
    if email.count("@") != 1 or email.count(".")!=1:
        return redirect("/email-error?user_name={0}&email={1}".format(user_name, email))
    if len(email)<3 or len(email)>20:
        return redirect("/email-error?user_name={0}&email={1}".format(user_name, email))
        
    return redirect("/successful-signup?user_name={0}".format(user_name))

@app.route("/username-error")
def username_error():
    error = "Invalid username"
    return render_template('edit.html', error1=error)

@app.route("/password-error")
def password_error():
    error = "Invalid password"
    user_name = request.args.get('user_name')
    email = request.args.get('email')
    return render_template('edit.html', user_name=user_name, email =email, error2=error)

@app.route("/verify-password-error")
def verify_password_error():
    error = "Passwords don't match"
    user_name = request.args.get('user_name')
    email = request.args.get('email')
    return render_template('edit.html', user_name=user_name, email=email, error3=error)

@app.route("/email-error")
def email_error():
    error = "Invalid email"
    user_name = request.args.get('user_name')
    email = request.args.get('email')
    return render_template('edit.html', user_name=user_name, email=email, error4=error)

@app.route("/successful-signup")
def successful_signup():
    user_name = request.args.get('user_name')
    return '<h1> Welcome '+ user_name +'</h1>'
@app.route("/")
def index():
    return render_template('edit.html')
app.run()