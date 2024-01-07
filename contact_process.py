from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        message = request.form['message']
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']

        # Email configuration
        to_email = 'Adetech062@gmail.com'
        smtp_server = 'your_smtp_server'
        smtp_port = 587  # Update with your SMTP server port
        smtp_username = 'your_email@example.com'
        smtp_password = 'your_email_password'

        # Email content
        email_content = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"

        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(email, to_email, email_content)

    return render_template('index.html')  # Replace with the path to your HTML file

if __name__ == '__main__':
    app.run(debug=True)
