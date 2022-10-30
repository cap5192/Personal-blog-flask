from flask import Flask, render_template, request
import requests
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

blog_data = requests.get("https://api.npoint.io/f7aafcffd3cebb66d65f").json()

@app.route('/')
def index():  # put application's code here
    return render_template("index.html", data=blog_data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/post/<int:num>')
def post(num):
    return render_template("post.html", post_number=num, data=blog_data)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == "POST":
        name = request.form['full_name']
        email = request.form["email_address"]
        phone_number = request.form['p_number']
        msg = request.form['message']

        message = Mail(
            from_email='cap5192@icloud.com',
            to_emails=email,
            subject='New Message',
            html_content=msg)

        sg = SendGridAPIClient('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')
        response = sg.send(message)

        return render_template("contact.html", flag=True)
    return render_template("contact.html", flag=False)

if __name__ == '__main__':
    app.run()
