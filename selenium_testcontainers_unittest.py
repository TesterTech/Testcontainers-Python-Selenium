import unittest

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from testcontainers.selenium import BrowserWebDriverContainer


class TestContainersTest(unittest.TestCase):

    def test_smoketest(self):
        with BrowserWebDriverContainer(DesiredCapabilities.CHROME) as chrome:
            webdriver = chrome.get_driver()
            webdriver.get("http://google.com")
            page_title = str(webdriver.title)
            webdriver.find_element(By.ID, "L2AGLb").click()
            self.assertEquals("Google", page_title)
            webdriver.find_element(By.NAME, "q").send_keys("This is a test!")
            webdriver.save_screenshot("./google.png")


if __name__ == '__main__':
    unittest.main()