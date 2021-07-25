import unittest
import GCodeParser

class GCodeParserTest(unittest.TestCase):
    
    def testGetLayerByComments(self):
        

        self.assertEqual(GCodeParser.getLayerByComments([]), [])

        data = []
        computedData = []

        self.assertEqual(GCodeParser.getLayerByComments(data), computedData)

unittest.main()