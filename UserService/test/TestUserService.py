import os
import sys
import unittest
import random

py_file_location = '/content/drive/MyDrive/HelloFreshOS/UserService/app'
sys.path.append(os.path.abspath(py_file_location))
import UserService as user

userid = random.randint(1000,9999)
id1 = "user" + str(userid)
user1 = {"id":id1, "firstName":"first", "lastName":"last"}
user2 = {"id":id1}
user3 = {"id":"user8"}

class TestUser(unittest.TestCase):

  def test_1SuccessUserCreation(self):
      response = user.create_user(user1)
      self.assertEqual(response[1],201)

  def test_2FailedUserCreation(self):
      response = user.create_user(user1)
      self.assertEqual(response[1],500)
  
  def test_3GetUserSuccess(self):
      response = user.get_user(user2)
      self.assertEqual(response[1],201)

  def test_4GetUserFailed(self):
      response = user.get_user(user3)
      self.assertEqual(response[1],500)
 
if __name__ == '__main__':
    unittest.main()