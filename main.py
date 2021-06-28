import requests
import api_helper
import gcode_parser
import key_reader
import simple_gui

import os
import sys

FORCE_SIMPLE = True

def main(argv):
    if "--nogui" in argv:
        pass
    elif "--simple" in argv or FORCE_SIMPLE:
        simple_gui.start()


if __name__ == "__main__":
    main(sys.argv[1:])