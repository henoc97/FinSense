# 📁 data/download_data.py

import yfinance as yf
import os
import pandas as pd

def download_stock_data(ticker: str, start_date: str, end_date: str, save_path: str):
    print(f"📥 Téléchargement des données pour {ticker} de {start_date} à {end_date}...")
    df = yf.download(ticker, start=start_date, end=end_date)

    if df.empty:
        print("⚠️ Aucune donnée téléchargée. Vérifie les dates ou le ticker.")
        return

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path)
    print(f"✅ Données sauvegardées dans {save_path}")

if __name__ == "__main__":
    TICKER = "TSLA"
    START_DATE = "2020-01-01"
    END_DATE = "2024-12-31"
    SAVE_PATH = "data/raw/tsla.csv"

    download_stock_data(TICKER, START_DATE, END_DATE, SAVE_PATH)
