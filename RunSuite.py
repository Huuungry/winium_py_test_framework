import os
import unittest

import HTMLTestRunner

from Test1 import Test_DSG

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
loaded_tests_1 = unittest.TestLoader().loadTestsFromTestCase(Test_DSG)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([loaded_tests_1])

# open the report file
outfile = open(dir + "\TestReport.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
                 stream=outfile,
                 title='Test Report',
                 description='Test'
                 )

# run the suite using HTMLTestRunner
runner.run(smoke_tests)