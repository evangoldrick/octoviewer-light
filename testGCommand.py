from GCommand import GCommand
import unittest
class testGCommand(unittest.TestCase):
    def testGCommand__eq__(self):
            self.assertEqual(GCommand(";", 0, 0), GCommand(";", 0, 0))
            self.assertNotEqual(GCommand("G1 X10.0", 0, 0), GCommand("G1 X1.0", 0, 0))

    def testGCommandIsLayerLabel(self):
        g = GCommand(";LAYER:1", 0, 0)
        self.assertTrue(g.isLayerLabel())

    def testGCommandIsNotLayerLabel(self):
        g = GCommand("G1 X1.0", 0, 0)
        self.assertFalse(g.isLayerLabel())

    def testGCommandGetLayerLabel(self):
        g = GCommand(";LAYER:1", 0, 0)
        self.assertEqual(g.getLayerLabel(), 1)
