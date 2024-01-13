from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
import config as config

engine = create_engine(config.DB_URL)

Base = declarative_base()
class Orders(Base):
    __tablename__ = 'Orders'
    id = Column(String(20), primary_key=True)
    user_id = Column(String(20))
    product_code = Column(String(20))
    customer_full_name = Column(String(100))
    product_name = Column(String(50))
    total_amount = Column(Float)
    created_time = Column(DateTime)
	
Base.metadata.create_all(engine)
print("Table 'Orders' created successfully.")
Session = sessionmaker(engine)

def insertOrder(new_order):
    try:
        session = Session()
        session.add(new_order)
        session.commit()
        return {"id": new_order.id, "user id": new_order.user_id, "product_code": new_order.product_code}, 200
    except Exception as e:
        print(f"The error '{e}' occurred.")
        return {"error": "An error occurred while creating the order."}, 500
