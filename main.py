from flask import Flask, render_template, url_for, send_from_directory,request
import smtplib

MY_EMAIL = "ameyaamanagi1809@gmail.com"
PASSWORD = "drbdbbelnwrxcqgx"

app = Flask(__name__)

def send_mail(name, email, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  
        connection.starttls()  
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:New Message\n\nName:{name}\nEmail:{email}\nMessage:{message}")

#Home Page
@app.route('/')
def home():
    return render_template('index.html')

#Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

#Skills and Certifications
@app.route('/skill_certification')
def skill_certification():
    return render_template('skill_certification.html')

#Download
@app.route('/download')

def download():
    return send_from_directory('static', path='files/resume2.pdf')

#Form
@app.route('/sendemail', methods=['POST'])
def sendemail():
    name = request.form['name']
    email = request.form['email_box']
    message = request.form['text_box']
    send_mail(name=name , email=email, message=message)
    return render_template('/email_send.html')

if __name__ =="__main__":
    app.run(debug=False)