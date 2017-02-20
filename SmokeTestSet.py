import os
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains


class Test_DSG(unittest.TestCase):
   WINIUM_PATH = r"C:\Utilities\SoftforAutomatization\Winium\Winium1.5\Winium.Desktop.Driver.exe"

   def setUp(self):
      for i in range(2):
         try:
            print("start driver creation")
            self.driver = webdriver.Remote('http://134.132.239.40:9999',
               {"debugConnectToRunningApp":"true"})
            print("driver created")
            # break
         except:
            print("Winium driver was not found")
            os.startfile(self.WINIUM_PATH)

   def test_cube_view(self):
      cube_view = self.driver.find_elements_by_name("Cube 1 (TVDSS)")
      print("Number of elements found: " + str(len(cube_view)))

      for elem in cube_view:
         print(elem.get_attribute("ClassName"))
         if (elem.get_attribute("ClassName")== None):
            elem.click()

   def test_inventory(self):
      inventory = self.driver.find_elements_by_name("Inventory")
      inventory.click()
      action = ActionChains(self.driver)
      action.context_click(inventory[1]).perform()

   def tearDown(self):
      self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)