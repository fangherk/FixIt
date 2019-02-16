import unittest

from test_matchingengine import TestMatchingEngine

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestMatchingEngine('test_empty_engine'))
    test_suite.addTest(TestMatchingEngine('test_add_order'))
    test_suite.addTest(TestMatchingEngine('test_match_simple_order'))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
