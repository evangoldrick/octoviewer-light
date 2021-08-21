import unittest
import time
import job_data_thread
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
        x = job_data_thread.JobDaemon()
        x.addFunction(tc.testFunction, num=1)
        x.start()
        time.sleep(0.1)
        x.stop()
        self.assertEqual(tc.val, 1)
        self.assertFalse(x.process.is_alive())

    def test2Execution(self):
        tc1 = testClass()
        tc2 = testClass()
        x = job_data_thread.JobDaemon()
        x.addFunction(tc1.testFunction, num=1)
        x.addFunction(tc2.testFunction, num=1)
        x.start()
        time.sleep(0.1)
        x.stop()
        self.assertEqual(tc1.val, 1)
        self.assertEqual(tc2.val, 1)
        self.assertFalse(x.process.is_alive())        
unittest.main()

