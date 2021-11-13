from flask import Flask, render_template, request
from flask_talisman import Talisman
import smtplib
import os

app = Flask(__name__)

# Should default all traffic to https
Talisman(app)

# Environment variables for encrypted user email and password.
userEmail = os.environ.get('USER_EMAIL')
userPass = os.environ.get('USER_PASS')

# Home page
@app.route("/")
def home():
    title = "Phoenix Air Services"
    return render_template("index.html", title=title)

# Contact Page
@app.route("/contact-us")
def contact():
    title = "Contact Us"
    return render_template("contact.html", title=title)

# Form page that gives the user an error or success message based on whether or not they put in all the information on the form.
@app.route("/form", methods=["POST"])
def form():
    # Variables for collecting the user information
    name = request.form.get("name")
    email = request.form.get("email")
    phone_number = request.form.get("phone")
    message = request.form.get("message")

    # Combining the collected user information into an array then joining the array together but spacing it out with \n\n
    customer_info = [name, email, phone_number, message]
    full_message = '\n\n'.join(customer_info)
    
    company_email = "Bobpairserv@aol.com"

    # Creating a server that uses the smtp port for gmail, logs into email I created, and sends an email to the company email variable made above.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(userEmail,userPass)

    # If statement to give the user an error if they do not put in all form fields as well as keep the information on the form fields that they did fill in as to not have
    # them fill it in again.

    if not name or not email or not phone_number or not message:
        error_statement = "All form fields required..."
        return render_template("contact.html", 
            error_statement=error_statement, name=name,
            email=email, 
            phone_number=phone_number, 
            message=message)
    else:
        
        # Sendmail(From select email, to the companies email, with the message that is joined together in the above variables)
        server.sendmail(userEmail, company_email, full_message)
        success_statement = "Your message has been sent succesfully!"

        return render_template("contact.html", success_statement=success_statement) 



if __name__ == "__main__":
    app.run(debug=True)