# Commented out lines show an example of what to add to have the
# runner.py file run all the tests.

import unittest
#from tests import test-file-name-here, other-test-file-name-here

loader = unittest.TestLoader()
suite = unittest.TestSuite()

#suite.addTests(loader.loadTestsFromModule(test-file-name-here))
#suite.addTests(loader.loadTestsFromModule(other-test-file-name-here))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)