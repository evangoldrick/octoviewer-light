import simple_gui
import tk_gui

import sys

FORCE_SIMPLE = False

def main(argv):
    if "--nogui" in argv:
        pass
    elif "--simple" in argv or FORCE_SIMPLE:
        simple_gui.start()
    else:
        tk_gui.start()


if __name__ == "__main__":
    main(sys.argv[1:])