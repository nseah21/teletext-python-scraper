from flask import Flask, jsonify
from scraper import scrape_data

app = Flask(__name__)

@app.get("/data")
def get_scraped_data():
    scraped_data = scrape_data()
    return jsonify(scraped_data)

def create_app():
    return app
