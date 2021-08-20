import unittest
import time
import job_data_daemon
class testClass:
    def __init__(self):
        self.resetVal()

    def resetVal(self):
        self.val = 0
        
    def testFunction(self, num):
        self.val = self.val + num

class JobDataDaemonTest(unittest.TestCase):

    def testExecution(self):
        tc = testClass()
        x = job_data_daemon.JobDaemon()
        x.addFunction(tc.testFunction, num=1)
        x.start()
        time.sleep(0.1)
        x.stop()
        self.assertEqual(tc.val, 1)
        self.assertFalse(x.daemon.is_alive())
        
unittest.main()

