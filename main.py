import api_helper
import gcode_parser
import keyReader

import PySimpleGUI as sg
import os
import sys


def main(argv):
    
    if not ("--nogui" in argv or "-g" in argv):
        print("init gui")

        infoPanelLayout = [[sg.Text("NONE", key="TIME/LAYER")], [sg.Text("NONE", key="-FILE NAME-")], [sg.Button("QUIT", key="QUIT")]]
        fullLayout = [[sg.Text("graph goes here", key="-IMAGE-")], [sg.ProgressBar(100, orientation="vertical", size=(600, 50), key="progress meter")], [sg.Column(infoPanelLayout)]]
        window = sg.Window(title="Octoviewer Light", layout=fullLayout, size=(1280,720))

        while True:

            # add api stuff

            event, values = window.read(timeout=1000)

            if event == "-QUIT-" or event == sg.WIN_CLOSED:
                print("EVENT LOOP EXIT")
                break

            window["progress meter"].update(float(api_helper.getResponse("http://octopi.local/api/job", keyReader.getKey()).json()["progress"]["completion"]))

        print("Close window")
        window.close()
            


if __name__ == "__main__":
    main(sys.argv[1:])