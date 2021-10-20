from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'Jaclem12@gmail.com'
# app.config['MAIL_PASSWORD'] = 'ovutdwridtgtjqxu'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)

@app.route("/")
def home():
    title = "Phoenix Air Services"
    return render_template("index.html", title=title)


@app.route("/contact-us")
def contact():
    title = "Contact Us"
    return render_template("contact.html", title=title)


@app.route("/form", methods=["POST"])
def form():
    first_name = request.form.get("fname")
    last_name = request.form.get("lname")

    full_name = first_name + " " + last_name

    email = request.form.get("email")
    phone_number = request.form.get("phone")
    message = request.form.get("message")

    customer_info = [full_name, email, phone_number, message]
    full_message = '\n\n'.join(customer_info)

    print(full_message)
    
    company_email = "Jaclem12@gmail.com"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("Jaclem12@gmail.com","ovutdwridtgtjqxu")
    server.sendmail("Jaclem12@gmail.com", company_email, full_message)

    if not first_name or not last_name or not email or not phone_number or not message:
        error_statement = "All form fields required..."
        return render_template("contact.html", 
            error_statement=error_statement, first_name=first_name, 
            last_name=last_name, 
            email=email, 
            phone_number=phone_number, 
            message=message)

    success_statement = "Your message has been sent succesfully!"
        

    return render_template("contact.html", success_statement=success_statement) 



if __name__ == "__main__":
    app.run(debug=True)