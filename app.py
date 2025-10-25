from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/pets", methods=["GET"])
def pets_list():
    return "pets list"

@app.route("/pets", methods=["POST"])
def pet_add():
    return "Pet has been added"

@app.route("/pets", methods=["PATCH"])
def pet_update():
    return "Pet has been updated"

@app.route("/pets", methods=["DELETE"])
def pet_update():
    return "Pet has been deleted"

@app.route("/pet_donate", methods=["POST"])
def pet_update():
    return "Pet has been deleted"