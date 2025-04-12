from flask import Flask, request, jsonify
from src.ufc_scraper import scrape_event  # Zorg dat deze functie klopt!

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        data = scrape_event(url)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Railway regelt hier zelf de juiste poort
    app.run(debug=True, host="0.0.0.0", port=port)