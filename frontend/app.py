# -*- coding: utf-8 -*-
"""
Created on Sat May  3 11:45:34 2025

@author: Jorge
"""

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    # Cargar los CSV generados por el script de análisis
    productos_disponibles = pd.read_csv("backend/productos_disponibles.csv").to_dict(orient="records")
    mas_baratos = pd.read_csv("backend/mas_baratos.csv").to_dict(orient="records")
    mas_caros = pd.read_csv("backend/mas_caros.csv").to_dict(orient="records")
    mas_vendidos = pd.read_csv("backend/mas_vendidos.csv").to_dict(orient="records")
    mejor_valorados = pd.read_csv("backend/mejor_valorados.csv").to_dict(orient="records")

    # Cargar el precio medio
    with open("backend/precio_medio.txt", "r") as f:
        precio_medio = f.read()

    return render_template(
        "index.html",
        productos=productos_disponibles,
        baratos=mas_baratos,
        caros=mas_caros,
        media=precio_medio,
        vendidos=mas_vendidos,
        rates=mejor_valorados
    )

if __name__ == "__main__":
    app.run(debug=True)
