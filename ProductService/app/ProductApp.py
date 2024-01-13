from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

import ProductService as product

from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app) 

@app.route("/products", methods=["GET"])
def get_product():
    data = request.get_json()
    return product.get_product(data)

@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    return product.add_product(data)

if __name__ == "__main__":
    app.run()