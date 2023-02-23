# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/22 20:06
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

    @file_data('../test_data/search.yaml')
    def test_01_login(self,**kwargs):
        self.driver.get_url(homepage)
        self.driver.move_to(**kwargs['move_to'])
        self.driver.click(**kwargs['click'])
        self.driver.swith_handle()
        self.driver.move_to(**kwargs['move_to1'])
        self.driver.click(**kwargs['click1'])
        self.driver.click(**kwargs['click2'])
        self.driver.swith_handle()
        self.assertIn('438',self.driver.get_text('xpath','//*[@id="maincontent"]/div[3]/div[2]/div[1]/dl/dd/div[3]/div/table/tbody/tr[8]/td[3]'))


if __name__ == '__main__':
    unittest.main()