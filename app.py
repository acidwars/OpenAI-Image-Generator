import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    result = False
    image_url = None
    if request.method == "POST":
        image = request.form["image"]
        response = openai.Image.create(
            prompt=image,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        result = image_url
        #return redirect(url_for("index", result=image_url))
        # return redirect(image_url)
    #result = request.args.get("result")
    result = image_url
    return render_template("index.html", result=result)


