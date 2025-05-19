from flask import Blueprint, render_template, redirect
import requests

main = Blueprint("main", __name__)

ESP32_IP = "192.168.0.229"  # Replace if it ever changes

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/toggle")
def toggle_ac():
    try:
        response = requests.get(f"http://{ESP32_IP}/toggle", timeout=3)
        print("ESP32 responded:", response.text)
    except requests.exceptions.RequestException as e:
        print("Failed to contact ESP32:", e)
    return redirect("/")