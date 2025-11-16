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
    chart_url = None
    error = None
    selected_symbol = None
    if request.method == "POST":
        selected_symbol = request.form.get("symbol") or request.form.get("symbol_text")
        if selected_symbol and " " in selected_symbol:
            selected_symbol = selected_symbol.split()[0].strip()
        try:
            if not selected_symbol:
                raise ValueError("No symbol provided")
            av = alphavantage_daily_series(selected_symbol, outputsize="compact")
            ts_key = None
            for k in av.keys():
                if "Time Series" in k:
                    ts_key = k
                    break
            if not ts_key:
                error = av.get("Note") or av.get("Error Message") or "Unexpected API response"
                raise RuntimeError(error)
            df = pd.DataFrame.from_dict(av[ts_key], orient='index')
            df = df.sort_index() 
            if '5. adjusted close' in df.columns:
                close_col = '5. adjusted close'
            elif '4. close' in df.columns:
                close_col = '4. close'
            else:
                raise RuntimeError("Cannot find close prices in API response")
            df.index = pd.to_datetime(df.index)
            df[close_col] = pd.to_numeric(df[close_col], errors='coerce')
            plt.figure(figsize=(10,4))
            plt.plot(df.index, df[close_col])
            plt.title(f"{selected_symbol} - Closing Price")
            plt.xlabel("Date")
            plt.ylabel("Price (USD)")
            plt.tight_layout()
            chart_path = os.path.join(app.static_folder, "chart.png")
            plt.savefig(chart_path)
            plt.close()
            chart_url = url_for('static', filename='chart.png') + f"?t={int(datetime.now().timestamp())}"
        except Exception as e:
            error = str(e)
    return render_template("index.html",
                           symbols=FALLBACK_SYMBOLS,
                           chart_url=chart_url,
                           error=error,
                           selected_symbol=selected_symbol)
@app.route("/search_symbols")
def search_symbols():
    return

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG", "0") == "1")