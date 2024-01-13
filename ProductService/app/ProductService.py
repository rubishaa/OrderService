from datetime import datetime
import ProductDBManager as db

def add_product(data):
    product_code = data["product_code"]
    product_name = data["product_name"]
    total_amount = data["total_amount"]
    new_product = db.Products(product_code=product_code,product_name=product_name,total_amount=total_amount)
   
    return db.insert_product(new_product)
             
def get_product(data):
    return db.get_product(data["product_code"]) 