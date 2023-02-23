import os
import time
import unittest
from HTMLTestReportCN import HTMLTestRunner  # （中文版）

# 配置测试报告信息
# 测试执行者：在HTMLTestReportCN报告中专属参数
report_tester = 'TGW'
# 保存路径
report_dir = './report/'
# 测试报告的title
report_title = 'TGW的测试报告'
# 描述
report_description = '这是测试报告的描述'
# 测试报告文件（路径，文件名）（文件名那里可以加个时间戳）
# 时间戳
t = time.strftime('%Y-%m-%d_%H-%M-%S')
report_file = report_dir + t + 'reportCN.html'
# 生成路径
# 如果这个路径不存在，就创建一个
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

path = './test_case'
discover = unittest.defaultTestLoader.discover(start_dir=path, pattern='test*.py')

# 生成HTMLTestRunner测试报告，本质意义上就是写入一个文件
with open(report_file, 'wb') as file:
    runner = HTMLTestRunner(stream=file, title=report_title,
                            description=report_description, verbosity=2, tester=report_tester)
    runner.run(discover)