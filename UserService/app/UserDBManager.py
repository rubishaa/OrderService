from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

dbURL = "postgresql://anet:vUdRee4BMHdbBaavGKEPefx9lwktPPO8@dpg-ckkv6f3j89us73bdu3q0-a.oregon-postgres.render.com/order_service"
engine = create_engine(dbURL)

Base = declarative_base()
class Users(Base):
    __tablename__ = 'Users'
    user_id = Column(String(20),primary_key=True)
    customer_first_name = Column(String(50))
    customer_last_name = Column(String(50))
	
	
Base.metadata.create_all(engine)
print("Table 'Users' created successfully.")
Session = sessionmaker(engine)

def get_user(user_id):
  try:
    session = Session()
    user = session.query(Users).filter(Users.user_id == user_id).first()
    return { "user_id":user.user_id,"customer_first_name":user.customer_first_name, "customer_last_name":user.customer_last_name}, 200
  except Exception as e:
    print(f"The error '{e}' occurred.")
    return {"error": "An error occurred while fetching the user/ no user exist."}, 500

def insert_user(new_user):
    try:
        session = Session()
        session.add(new_user)
        session.commit()
        return {"user_id": new_user.user_id}, 201
    except Exception as e:
        print(f"The error '{e}' occurred.")
        return {"error": "An error occurred while creating the user."}, 500

  