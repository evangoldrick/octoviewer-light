from g_command import GCommand
import unittest
import g_code_parser

TEST_GCODE_FILE = "testGCode.gcode"

class GCodeParserTest(unittest.TestCase):
    
    def testGetLayerByComments(self):
        # Test data and expected output
        data = [GCommand(";LAYER:0", 0, 0), GCommand("G1 X1.0", 50, 0), GCommand(";LAYER:1", 75, 1), GCommand("G1 X2.0", 100, 1)]
        computedData = [[GCommand(";LAYER:0", 0, 0), GCommand("G1 X1.0", 50, 0)], [GCommand(";LAYER:1", 75, 1), GCommand("G1 X2.0", 100, 1)]]

        self.assertEqual(g_code_parser.getLayerByComments(data), computedData) # Use test data

    def testParseCommandBlankComment(self):
        g = GCommand(";", 0)
        self.assertEqual(g.command, ";")
        self.assertEqual(g.parameters, dict({0:""}))
        self.assertEqual(g.byteCount, 0)
        self.assertEqual(g.layer, None)

    def testParseCommandComment(self):
        g = GCommand(";Comment", 0, 0)
        self.assertEqual(g.command, ";")
        self.assertEqual(g.parameters, dict({0:"Comment"}))
        self.assertEqual(g.byteCount, 0)
        self.assertEqual(g.layer, 0)
        
    def testGetParsedFileByCommentsComment(self):
        parsedFile = g_code_parser.getParsedFileByComments(TEST_GCODE_FILE)
        self.assertIn(GCommand(";FLAVOR:Marlin", 0, 0), parsedFile[0])

    def testGetParsedFileByCommentsCommand(self):
        parsedFile = g_code_parser.getParsedFileByComments(TEST_GCODE_FILE)
        self.assertIn(GCommand("G1 F4500 X109.291 Y93.05 E50.51166", 400, 1), parsedFile[1])
