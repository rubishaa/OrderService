from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
import OrderService as order


from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app) 

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    return order.create_order(data)

if __name__ == "__main__":
    app.run()