from datetime import datetime
import OrderDBManager as db
import OrderMQHandler as mq
import requests
import json
import config as config

uniqueID = 0

def create_order(data):
  try:
      product_code = data["product_code"]
      user_id = data["user_id"]
      global uniqueID
      uniqueID +=1
      id = product_code + user_id + str(uniqueID)
      customer_full_name = get_user(user_id)
      product = get_product(product_code)

      if (customer_full_name =="") or (product ==""):
        return {"error": "Invalid product code or user id."}, 500

      product_name = product[0]
      total_amount = product[1]
      created_time = datetime.now()

      dt_str = created_time.strftime("%Y-%m-%d %H:%M:%S") 
      new_order = db.Orders(id=id,product_code=product_code,user_id=user_id,customer_full_name=customer_full_name,product_name=product_name,total_amount=total_amount,created_time=created_time)
      msg = [id,product_code,user_id,customer_full_name,product_name,total_amount,dt_str]
      
      if(mq.publish_orderMsg('created_order',msg)):
        print("Successfully Published")
      else:
        print("Error occured in publish. Message Cached")

      return db.insertOrder(new_order)

  except Exception as e:
      print(f"The error '{e}' occurred.")
      return {"error": "An error occurred while creating the order."}, 500
        
def get_user(user_id):
    url = config.USER_URL
    try:
      obj = {'id': user_id}
      response =  requests.get(url,json = obj)
      data = response.json()
      json.dumps(data)
      return data["firstName"] + " " + data["lastName"]
    except Exception as e:
      print(f"The error '{e}' occurred.")
      return ""
      
    
def get_product(product_code):
    url = config.PRODUCT_URL
    try:
      obj = {'code': product_code}
      response =  requests.get(url,json = obj)
      data = response.json()
      json.dumps(data)
      return data["name"],data["price"]
    except Exception as e:
      print(f"The error '{e}' occurred.")
      return "" 