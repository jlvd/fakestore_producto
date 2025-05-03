# -*- coding: utf-8 -*-
"""
Created on Sat May  3 11:31:18 2025

@author: Jorge
"""


import requests
import pandas as pd

# Obtener todos los productos
response = requests.get("https://fakestoreapi.com/products")
products = response.json()

# Convertir en DataFrame
df = pd.DataFrame(products)

# Asegurarse de que los ratings estén en columnas separadas
df["rate"] = df["rating"].apply(lambda x: x["rate"])
df["count"] = df["rating"].apply(lambda x: x["count"])

# 1. Productos disponibles
productos_disponibles = df[["id", "title", "price", "description", "category", "image"]]

# 2. Productos más baratos (Top 5)
mas_baratos = df.nsmallest(5, "price")[["title", "price", "image"]]

# 3. Productos más caros (Top 5)
mas_caros = df.nlargest(5, "price")[["title", "price", "image"]]

# 4. Precio medio
precio_medio = round(df["price"].mean(), 2)

# 5. Productos más vendidos (Top 5 por rating.count)
mas_vendidos = df.nlargest(5, "count")[["title", "count", "image"]]

# 6. Productos con mayor rate (Top 5 por rating.rate)
mejor_valorados = df.nlargest(5, "rate")[["title", "rate", "image"]]

# Exportar resultados a CSV para usarlos desde el frontend
productos_disponibles.to_csv("backend/productos_disponibles.csv", index=False)
mas_baratos.to_csv("backend/mas_baratos.csv", index=False)
mas_caros.to_csv("backend/mas_caros.csv", index=False)
mas_vendidos.to_csv("backend/mas_vendidos.csv", index=False)
mejor_valorados.to_csv("backend/mejor_valorados.csv", index=False)

# Guardar la media como archivo de texto simple
with open("backend/precio_medio.txt", "w") as f:
    f.write(str(precio_medio))
