from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

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
    name = request.form.get("name")

    email = request.form.get("email")
    phone_number = request.form.get("phone")
    message = request.form.get("message")

    customer_info = [name, email, phone_number, message]
    full_message = '\n\n'.join(customer_info)

    print(full_message)
    
    company_email = "bobpairserv@aol.com"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("phoenixairhvac@gmail.com","G1Zw7jA7tzoZ")
    server.sendmail("phoenixairhvac@gmail.com", company_email, full_message)

    if not name or not email or not phone_number or not message:
        error_statement = "All form fields required..."
        return render_template("contact.html", 
            error_statement=error_statement, name=name,
            email=email, 
            phone_number=phone_number, 
            message=message)

    success_statement = "Your message has been sent succesfully!"

    return render_template("contact.html", success_statement=success_statement) 



if __name__ == "__main__":
    app.run(debug=True)