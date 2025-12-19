from flask import Flask,render_template , request , redirect
from flask_mail import Mail,Message
import os
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']=os.getenv('SEN_EMAIL')
app.config['MAIL_PASSWORD']=os.getenv('PASSWORD')
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail = Mail(app)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/submit" , methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        msg = Message(subject="New Contact Message",sender=os.getenv("SEN_EMAIL") , recipients=[os.getenv("REC_EMAIL")])
        msg.body ="Email id: "+ email + "\n" +"Name: " + name +"\n\n" + message
        mail.send(msg)
        return render_template("index.html")
    else:
        return render_template("index.html")

app.run(debug=True)