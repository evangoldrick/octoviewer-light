import requests
import ApiHelper
import GCodeParser
import KeyReader
import SimpleGui
import TkGui

import os
import sys

FORCE_SIMPLE = False

def main(argv):
    if "--nogui" in argv:
        pass
    elif "--simple" in argv or FORCE_SIMPLE:
        SimpleGui.start()
    else:
        TkGui.start()


if __name__ == "__main__":
    main(sys.argv[1:])