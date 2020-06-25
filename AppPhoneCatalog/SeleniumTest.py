import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def test_LoginAndAddInform(self):
        self.driver.get("http://127.0.0.1:8080/AppPhoneCatalog")
        time.sleep(2)
        elem = self.driver.find_element_by_link_text("Log in")
        elem.click()
        time.sleep(2)
        elem=self.driver.find_element_by_xpath("//input [@name='username']")
        elem.send_keys("Denis")
        time.sleep(2)
        elem = self.driver.find_element_by_xpath("//input [@name='password']")
        elem.send_keys("11121987d")
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        self.assertIn("Admin panel", self.driver.page_source)
        time.sleep(2)
        elem= self.driver.find_element_by_link_text("Admin panel")
        elem.click()
        time.sleep(3)
        self.assertIn("Add Inform:", self.driver.page_source)
        elem = self.driver.find_element_by_xpath("//input [@name='NameCompany']")
        elem.send_keys("AddNewTest")
        time.sleep(3)
        elem= self.driver.find_element_by_xpath("//input [@name='Adress']")
        elem.send_keys("Minsk")
        time.sleep(3)
        elem=self.driver.find_element_by_xpath("//input [@name='Phone']")
        elem.send_keys("801234211")
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertIn("Chat",self.driver.page_source)
        elem = self.driver.find_element_by_link_text("Log out")
        elem.click()
        time.sleep(5)
        self.assertIn("Log in", self.driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
