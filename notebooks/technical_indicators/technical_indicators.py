#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Calcul des indicateurs techniques pour l'analyse financière
"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_sma(df, window=20):
    """Calcule la Simple Moving Average (SMA)"""
    return df['Close'].rolling(window=window).mean()

def calculate_ema(df, window=20):
    """Calcule l'Exponential Moving Average (EMA)"""
    return df['Close'].ewm(span=window, adjust=False).mean()

def calculate_rsi(df, window=14):
    """Calcule le Relative Strength Index (RSI)"""
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_macd(df, fast=12, slow=26, signal=9):
    """Calcule le Moving Average Convergence Divergence (MACD)"""
    exp1 = df['Close'].ewm(span=fast, adjust=False).mean()
    exp2 = df['Close'].ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    histogram = macd - signal_line
    return macd, signal_line, histogram

def calculate_bollinger_bands(df, window=20, num_std=2):
    """Calcule les bandes de Bollinger"""
    sma = calculate_sma(df, window)
    std = df['Close'].rolling(window=window).std()
    upper_band = sma + (std * num_std)
    lower_band = sma - (std * num_std)
    return upper_band, sma, lower_band

def calculate_stochastic(df, window=14, smooth_window=3):
    """Calcule l'oscillateur stochastique"""
    low_min = df['Low'].rolling(window=window).min()
    high_max = df['High'].rolling(window=window).max()
    k = 100 * ((df['Close'] - low_min) / (high_max - low_min))
    d = k.rolling(window=smooth_window).mean()
    return k, d

def plot_technical_indicators(df, indicators):
    """Crée un graphique interactif avec les indicateurs techniques"""
    # Création du graphique avec subplots
    fig = make_subplots(rows=4, cols=1, 
                       shared_xaxes=True,
                       vertical_spacing=0.05,
                       row_heights=[0.4, 0.2, 0.2, 0.2])

    # Graphique des prix et bandes de Bollinger
    fig.add_trace(go.Candlestick(x=df.index,
                                open=df['Open'],
                                high=df['High'],
                                low=df['Low'],
                                close=df['Close'],
                                name='OHLC'),
                  row=1, col=1)

    if 'bollinger' in indicators:
        fig.add_trace(go.Scatter(x=df.index, y=indicators['bollinger']['upper'],
                                name='Bande supérieure',
                                line=dict(color='gray', dash='dash')),
                      row=1, col=1)
        fig.add_trace(go.Scatter(x=df.index, y=indicators['bollinger']['middle'],
                                name='SMA 20',
                                line=dict(color='blue')),
                      row=1, col=1)
        fig.add_trace(go.Scatter(x=df.index, y=indicators['bollinger']['lower'],
                                name='Bande inférieure',
                                line=dict(color='gray', dash='dash')),
                      row=1, col=1)

    # RSI
    if 'rsi' in indicators:
        fig.add_trace(go.Scatter(x=df.index, y=indicators['rsi'],
                                name='RSI',
                                line=dict(color='purple')),
                      row=2, col=1)
        # Lignes de survente/surachat
        fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
        fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)

    # MACD
    if 'macd' in indicators:
        fig.add_trace(go.Scatter(x=df.index, y=indicators['macd']['macd'],
                                name='MACD',
                                line=dict(color='blue')),
                      row=3, col=1)
        fig.add_trace(go.Scatter(x=df.index, y=indicators['macd']['signal'],
                                name='Signal',
                                line=dict(color='orange')),
                      row=3, col=1)
        fig.add_trace(go.Bar(x=df.index, y=indicators['macd']['histogram'],
                            name='Histogramme',
                            marker_color='gray'),
                      row=3, col=1)

    # Stochastique
    if 'stochastic' in indicators:
        fig.add_trace(go.Scatter(x=df.index, y=indicators['stochastic']['k'],
                                name='%K',
                                line=dict(color='blue')),
                      row=4, col=1)
        fig.add_trace(go.Scatter(x=df.index, y=indicators['stochastic']['d'],
                                name='%D',
                                line=dict(color='orange')),
                      row=4, col=1)
        # Lignes de survente/surachat
        fig.add_hline(y=80, line_dash="dash", line_color="red", row=4, col=1)
        fig.add_hline(y=20, line_dash="dash", line_color="green", row=4, col=1)

    # Mise à jour du layout
    fig.update_layout(
        title='Indicateurs Techniques TSLA',
        yaxis_title='Prix ($)',
        yaxis2_title='RSI',
        yaxis3_title='MACD',
        yaxis4_title='Stochastique',
        xaxis_rangeslider_visible=False,
        height=1000
    )

    return fig

def calculate_all_indicators(df):
    """Calcule tous les indicateurs techniques"""
    indicators = {}
    
    # Moyennes mobiles
    indicators['sma_20'] = calculate_sma(df, 20)
    indicators['sma_50'] = calculate_sma(df, 50)
    indicators['ema_20'] = calculate_ema(df, 20)
    
    # RSI
    indicators['rsi'] = calculate_rsi(df)
    
    # MACD
    macd, signal, hist = calculate_macd(df)
    indicators['macd'] = {
        'macd': macd,
        'signal': signal,
        'histogram': hist
    }
    
    # Bandes de Bollinger
    upper, middle, lower = calculate_bollinger_bands(df)
    indicators['bollinger'] = {
        'upper': upper,
        'middle': middle,
        'lower': lower
    }
    
    # Stochastique
    k, d = calculate_stochastic(df)
    indicators['stochastic'] = {
        'k': k,
        'd': d
    }
    
    return indicators

def main(df):
    """Fonction principale"""
    # Calcul de tous les indicateurs
    indicators = calculate_all_indicators(df)
    
    # Création du graphique
    fig = plot_technical_indicators(df, indicators)
    
    # Sauvegarde du graphique
    fig.write_html('../notebooks/technical_analysis.html')
    
    # Création d'un DataFrame avec tous les indicateurs
    indicators_df = pd.DataFrame({
        'SMA_20': indicators['sma_20'],
        'SMA_50': indicators['sma_50'],
        'EMA_20': indicators['ema_20'],
        'RSI': indicators['rsi'],
        'MACD': indicators['macd']['macd'],
        'MACD_Signal': indicators['macd']['signal'],
        'BB_Upper': indicators['bollinger']['upper'],
        'BB_Middle': indicators['bollinger']['middle'],
        'BB_Lower': indicators['bollinger']['lower'],
        'Stoch_K': indicators['stochastic']['k'],
        'Stoch_D': indicators['stochastic']['d']
    })
    
    # Sauvegarde des indicateurs
    indicators_df.to_csv('../notebooks/technical_indicators.csv')
    
    return indicators

if __name__ == "__main__":
    # Chargement des données
    from eda_analysis import load_data
    df = load_data('../data/raw/tsla.csv')
    
    # Calcul des indicateurs
    indicators = main(df) 