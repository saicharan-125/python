from flask import *
from flask_mail import *
from flask_mysqldb import MySQL
from random import *

app = Flask(__name__)
app.secret_key = "abc123"

app.secret_key="keyvalue"
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="project"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql = MySQL(app)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USERNAME"] = "jayanthkaruparti.CCBPian00101@gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_PASSWORD"] = "smmevefjkfhijjmt"
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USE_TLS"] = False
mail = Mail(app)

otp = randint(000000,999999)

@app.route("/")
def homep():
    return render_template("overseas.html")

@app.route("/userflash")
def userflash():
    return render_template("userflash.html")



@app.route("/adminflash")
def adminflash():
    return render_template("adminflash.html")


@app.route("/home")
def home():
    return render_template('overseas.html')
@app.route("/intake")
def intake():
    return render_template('intake.html')

@app.route("/country")
def country():
    return render_template('country.html')

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/notifications")
def notifications():
    return render_template("notifications.html")

@app.route("/universitiesapplied")
def universitiesapplied():
    return render_template("universitiesapplied.html")

@app.route("/universitiesapproved")
def universitiesapproved():
    return render_template("universitiesapproved.html")

@app.route("/adprofile")
def adprofile():
    return render_template("adprofile.html")

@app.route("/student")
def student():
    return render_template("student.html")
@app.route("/studentstatus")
def studentstatus():
    return render_template("studentstatus.html")

@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        fathername = request.form['fathername']
        contact = request.form['contact']
        email = request.form['email']
        msg = Message('subject', sender="jayanthkaruparti.CCBPian00101@gmail.com", recipients=[email])
        msg.body = "THIS IS YOUR OTP" + str(otp)
        mail.send(msg)
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        qualification = request.form['qualification']
        location = request.form['location']
        gender = request.form['gender']
        maritial = request.form['maritial']
        reference = request.form['reference']
        cur = mysql.connection.cursor()
        br = cur.execute('insert into usertable(username,firstname,lastname,fathername,contact,email,password,confirmpassword,qualification,location,gender,maritial,reference) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(username,firstname,lastname,fathername,contact,email,password,confirmpassword,qualification,location,gender,maritial,reference))
        mysql.connection.commit()
        if br > 0 :
            if password == confirmpassword:
                flash("Registration successful check for otp ")
                return redirect(url_for("userflash"))
            else:
                error = "something went wrong"
                return render_template("register.html",error = error)
        else:
            error = "oops something went wrong"
            return render_template("overseas.html",error = error)
        cur.close()
    return render_template("register.html")


@app.route("/admin_register",methods=['GET','POST'])
def admin_register():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        br=cur.execute("insert into admintable(email,password) values(%s,%s)",(email,password))
        mysql.connection.commit()
        if br>0:
            flash("Admin Register successfull")
            return redirect(url_for("adminflash"))
        else:
            error = "oops something went wrong"
            return render_template("admin_register.html",error = error)

        cur.close()

    return render_template("admin_register.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        b = cur.execute('select email,password from usertable where email = %s and password = %s ',(email,password))
        mysql.connection.commit()
        if b > 0:
            result = cur.fetchone()
            print(result)
            username1 = result['email']
            session.permanent = True
            session['email'] = email
            password1 = result['password']
            if username1 == email and password1 == password:
                flash("successful logged in")
                return redirect(url_for("student"))
            else:
                error = "oops!something went wrong"
                return render_template("login.html", error=error)
        else:
            error = "oops something went wrong"
            return render_template("login.html",error=error)
    else:
        if 'email' in session:
            email = session["email"]
            return redirect(url_for('student'))
        else:
            return render_template('login.html')
        cur.close()
    return render_template("login.html")

@app.route('/admin_login', methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email)
        print(password)
        cur = mysql.connection.cursor()
        c = cur.execute('select password,email from admintable where  password = %s and email =%s',(password,email))
        mysql.connection.commit()
        if c > 0:
            result = cur.fetchone()
            print(result)
            username1 = result['email']
            session.permanent = True
            session['email'] = email
            password1 = result['password']
            if username1 == email and password1 == password:
                flash("successful logged in")
                return redirect(url_for("admin_dashboard"))
            else:
                error = "oops!something went wrong"
                return render_template("register.html", error=error)
        else:
            error = "oops something went wrong"
            return render_template("admin_login.html", error=error)
    else:
        if 'email' in session:
            email = session["email"]
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin_login.html')
        cur.close()
    return render_template("admin_login.html")

@app.route("/addadmin",methods=['GET','POST'])
def addadmin():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'admin':
            return redirect(url_for("admin_register"))
        else:
            return "Wrong password"
    return render_template('addadmin.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/validate',methods=['POST'])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return redirect(url_for("login"))

    else:
        error = "wrong OTP"
        return render_template("send.html", error=error)
    cur
@app.route("/send")
def send():
    return render_template("send.html")

@app.route("/dbfetch")
def user():
    cur = mysql.connection.cursor()
    r = cur.execute('select * from usertable')
    mysql.connection.commit()
    if r>0:
        re = cur.fetchall()
        print(re)
        return render_template("dbfetch.html",result=re)
    cur.close()
    return render_template("dbfetch.html")

if __name__ == "__main__":
    app.run(debug="True")