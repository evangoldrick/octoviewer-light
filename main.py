import requests
import ApiHelper
import GCodeParser
import KeyReader
import SimpleGui

import os
import sys

FORCE_SIMPLE = True

def main(argv):
    if "--nogui" in argv:
        pass
    elif "--simple" in argv or FORCE_SIMPLE:
        SimpleGui.start()


if __name__ == "__main__":
    main(sys.argv[1:])