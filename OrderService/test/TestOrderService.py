import os
import sys
import unittest
import random

py_file_location = '/content/drive/MyDrive/HelloFreshOS/OrderService/app'
sys.path.append(os.path.abspath(py_file_location))
import OrderService as order

Order1 = {"user_id": "7c11e1ce2741","product_code": "classic-box"}
Order2 = {"user_id": "7c11e1ce2741","product_code": "family-box"}
Order3 = {"user_id": "7c11e1ce2741","product_code": "veggie-box"}
Order4 = {"user_id": "e6f24d7d1c7e","product_code": "classic-box"}
Order5 = {"user_id": "e6f24d7d1c7e","product_code": "family-box"}
Order6 = {"user_id": "e6f24d7d1c7e","product_code": "veggie-box"}

class TestOrder(unittest.TestCase):

  def test_Order1(self):
      response = order.create_order(Order1)
      self.assertEqual(response[1],200)

  def test_Order2(self):
      response = order.create_order(Order1)
      self.assertEqual(response[1],200)
  
  def test_Order3(self):
      response = order.create_order(Order3)
      self.assertEqual(response[1],500)

  def test_Order4(self):
      response = order.create_order(Order4)
      self.assertTrue(response[1]==200 or response[1]==500)

  def test_Order5(self):
      response = order.create_order(Order5)
      self.assertTrue(response[1]==200 or response[1]==500)

  def test_Order6(self):
      response = order.create_order(Order6)
      self.assertEqual(response[1],500)
 
if __name__ == '__main__':
    unittest.main()