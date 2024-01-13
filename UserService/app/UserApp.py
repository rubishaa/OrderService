from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
import UserService as user

from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app) 

@app.route("/users", methods=["GET"])
def get_user():
    data = request.get_json()
    return user.get_user(data)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    return user.create_user(data)

if __name__ == "__main__":
    app.run()