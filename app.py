from flask import Flask, render_template, request

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
    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    email = request.form.get("email")
    phone_number = request.form.get("phone")
    message = request.form.get("message")

    if not first_name or not last_name or not email or not phone_number or not message:
        error_statement = "All form fields required..."
        return render_template("contact.html", 
            error_statement=error_statement, first_name=first_name, 
            last_name=last_name, 
            email=email, 
            phone_number=phone_number, 
            message=message)

    return render_template("contact.html") 

if __name__ == "__main__":
    app.run(debug=True)