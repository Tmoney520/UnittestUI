# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/22 19:45
# @Author :TGW
"""
import unittest

from ddt import ddt,file_data

from VAR.URL import homepage
from common.webkeys import Keys

@ddt
class Demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = Keys('Chrome')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit_browser()

    def test_01_login(self):
        self.driver.get_url(homepage)
        self.driver.move_to('link text','教学科研')
        self.driver.click('link text','教学')
        self.driver.click('link text','教学日历')
        self.driver.swith_handle()
        self.assertEqual('2022-2023学年校历',self.driver.get_title())


if __name__ == '__main__':
    unittest.main()