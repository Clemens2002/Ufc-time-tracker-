# main.py

from flask import Flask, request, jsonify
from src.ufc_scraper import scrape_event  # Zorg dat dit pad klopt met jouw projectstructuur
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "UFC Scraper API draait!"

@app.route("/event", methods=["GET"])
def get_event():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Geen URL opgegeven"}), 400

    try:
        data = scrape_event(url)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway geeft automatisch de juiste poort door
    app.run(debug=True, host="0.0.0.0", port=port)