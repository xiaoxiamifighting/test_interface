import unittest

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome import webdriver


class Test_day1(unittest.TestCase):
    def setUp(self):
        # 远程Remote server
        self.driver = webdriver.remote(desired_capabilities=DesiredCapabilities.CHROME)

