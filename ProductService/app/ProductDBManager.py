from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

dbURL = "postgresql://anet:vUdRee4BMHdbBaavGKEPefx9lwktPPO8@dpg-ckkv6f3j89us73bdu3q0-a.oregon-postgres.render.com/order_service"
engine = create_engine(dbURL)

Base = declarative_base()
class Products(Base):
    __tablename__ = 'Products'
    product_code = Column(String(20),primary_key=True)
    product_name = Column(String(50))
    total_amount = Column(Float)
		
Base.metadata.create_all(engine)
print("Table 'Products' created successfully.")
Session = sessionmaker(engine)

def get_product(product_code):
  try:
    session = Session()
    product = session.query(Products).filter(Products.product_code == product_code).first()
    return { "product_code":product.product_code,"product_name": product.product_name,"total_amount":product.total_amount}, 200
  except Exception as e:
    print(f"The error '{e}' occurred.")
    return {"error": "An error occurred while fetching the product/ no product exist."}, 500

def insert_product(new_product):
    try:
        session = Session()
        session.add(new_product)
        session.commit()
        return {"product_code": new_product.product_code}, 201
    except Exception as e:
        print(f"The error '{e}' occurred.")
        return {"error": "An error occurred while creating the product."}, 500
 