## IT 4320 Project 3b
#Aidan Engbert
#NAME
#NAME
#NAME

import os
import io
from flask import Flask, render_template, request, send_from_directory, jsonify, url_for
import requests
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime

API_KEY = "Y1VTX9XT399MJE42"
BASE_URL = "https://www.alphavantage.co/query"

app = Flask(__name__, static_folder="static", template_folder="templates")

def alphavantage_symbol_search(keywords):
    return

def alphavantage_daily_series(symbol, outputsize="compact"):
    return

def index():
    return

def search_symbols():
    return

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG", "0") == "1")