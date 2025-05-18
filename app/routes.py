from flask import Blueprint, render_template, request, redirect

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/toggle")
def toggle_ac():
    # You'd add ESP32 interaction here
    print("Toggling AC!")
    return redirect("/")