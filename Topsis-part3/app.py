from flask import Flask, render_template, request
import os
import re
from topsis_logic import run_topsis
from flask import flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = "secret"

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]

        if not is_valid_email(email):
            return "Invalid email format"

        weights = weights.split(",")
        impacts = impacts.split(",")

        if len(weights) != len(impacts):
            return "Weights and impacts count must be equal"

        if not all(i in ["+", "-"] for i in impacts):
            return "Impacts must be + or -"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "result.csv")

        file.save(input_path)

        run_topsis(input_path, weights, impacts, output_path)

        send_email(email, output_path)

        return "Result sent to your email successfully!"

    return render_template("index.html")

def send_email(receiver, file_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = "your_email@gmail.com"
    msg["To"] = receiver
    msg.set_content("Please find the attached TOPSIS result file.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("anandarshia8613@gmail.com", "vxgqivwxresurzat")
        server.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)


