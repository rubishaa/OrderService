from datetime import datetime
import UserDBManager as db
#import UserMQHandler as mq

def create_user(data):
    uid = data["id"]
    firstName = data["firstName"]
    lastName = data["lastName"]

    new_user = db.Users(uid=uid,firstName=firstName,lastName=lastName)
 
    return db.insert_user(new_user)
        
def get_user(data):
    return db.get_user(data["id"]) 