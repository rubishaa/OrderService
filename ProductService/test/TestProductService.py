import os
import sys
import unittest
import random

py_file_location = '/content/drive/MyDrive/HelloFreshOS/ProductService/app'
sys.path.append(os.path.abspath(py_file_location))
import ProductService as product

productid = random.randint(1000,9999)
product_id = "product" + str(productid)
prod1 = {"product_code":product_id, "product_name":"first","total_amount":"5"}
prod2 = {"product_code":product_id}
prod3 = {"product_code":"prod8"}

class TestProduct(unittest.TestCase):

  def test_1SuccessProductCreation(self):
      response = product.add_product(prod1)
      self.assertEqual(response[1],201)

  def test_2FailedProductCreation(self):
      response = product.add_product(prod1)
      self.assertEqual(response[1],500)
  
  def test_3GetProductSuccess(self):
      response = product.get_product(prod2)
      self.assertEqual(response[1],201)

  def test_4GetProdcutFailed(self):
      response = product.get_product(prod3)
      self.assertEqual(response[1],500)
 
if __name__ == '__main__':
    unittest.main()