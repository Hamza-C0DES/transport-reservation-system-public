import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Pull the private data, but have a generic backup just in case
app.config["COMPANY_NAME"] = os.getenv("COMPANY_NAME", "Demo Transport Co.")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default-dev-key")
app.config["IMAGE_PATH"] = os.getenv("IMAGE_PATH", "static/images/default-image.png")
# app.config["IMAGE"] = os.getenv("IMAGE", "static/images/default-image.png")

@app.route("/")
def home():
    business_name = app.config["COMPANY_NAME"]
    image_path = app.config["IMAGE_PATH"]
    #image = app.config["IMAGE"]
    return render_template("home.html", company = business_name, image_path=image_path) #, image=image)