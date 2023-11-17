from flask import Flask, render_template, redirect, session, request
from werkzeug.utils import secure_filename
from flask_session import Session
import requests
import os
import base64


app = Flask(__name__)
# Autoreloading page if change in html file
app.config["TEMPLATES_AUTO_RELOAD"] = True

#Implementing cookies -
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["GET", "POST"])
def process():
    '''
    complete this to validate the file submission -
    if 'myFile' not in request.files:
        return 'No file part'
    '''
    #file = request.files['myFile']
    '''
    Another validation
    if file.filename == '':
        return 'No selected file'
    '''
#loerwubtv8wo6gpo85vq3bo483vbotg68v
    if request.method == "POST":
        file = request.files['myFile']
        file.save(file.filename)
        saved_image = str(file.filename)

        # Client ID : cfe153e15385fc3
        # Set API endpoint and headers
        url = "https://api.imgur.com/3/image"
        headers = {"Authorization": "Client-ID cfe153e15385fc3"}

        # Read image file and encode as base64
        with open(saved_image, "rb") as file:
            data = file.read()
            base64_data = base64.b64encode(data)

        # Upload image to Imgur and get URL
        response = requests.post(url, headers=headers, data={"image": base64_data})
        image_url = response.json()["data"]["link"]

        os.remove(saved_image)

        # after getting the image url, send to to OCR scanner
        url = "https://ocr-extract-text.p.rapidapi.com/ocr"

        querystring = {"url":image_url}

        headers = {
            "X-RapidAPI-Key": "d5e1035c76msh634d96656174316p1f9e0ejsnc9dd4bb11da0",
            "X-RapidAPI-Host": "ocr-extract-text.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        imp_content = (response.json())['text']


        ingr_url = "https://recipe-finder3.p.rapidapi.com/icecream/recipes"

        ingr_querystring = {"ingredient":imp_content}

        ingr_headers = {
            "X-RapidAPI-Key": "d5e1035c76msh634d96656174316p1f9e0ejsnc9dd4bb11da0",
            "X-RapidAPI-Host": "recipe-finder3.p.rapidapi.com"
        }

        ingr_response = requests.get(ingr_url, headers=ingr_headers, params=ingr_querystring)

        my_ingredients_list = (ingr_response.json())['ingredients']
        my_instruction_list = (ingr_response.json())['instructions']

        return render_template("process.html", ingredients=my_ingredients_list, instructions = my_instruction_list)

    else:
        return render_template("index.html")





