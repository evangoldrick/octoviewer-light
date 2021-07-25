import ApiHelper
import KeyReader
import requests
import PySimpleGUI as sg

def start():
    print("init simple gui")

    infoPanelLayout = [[sg.Text("NONE", key="TIME/LAYER")], [sg.Text("NONE", key="-FILE NAME-")], [sg.Button("QUIT", key="QUIT")]]
    fullLayout = [[sg.Text("graph goes here", key="-IMAGE-")], [sg.ProgressBar(100, orientation="vertical", size=(600, 50), key="progress meter")], [sg.Column(infoPanelLayout)]]
    window = sg.Window(title="Octoviewer Light", layout=fullLayout, size=(1280,720))

    while True:

        # add api stuff

        event, values = window.read(timeout=5000)

        if event == "-QUIT-" or event == sg.WIN_CLOSED:
            print("EVENT LOOP EXIT")
            break
        try:
            respJSON = ApiHelper.getResponse("http://octopi.local/api/job", KeyReader.getKey()).json()
            
            if respJSON["progress"]["completion"] is not None:
                window["progress meter"].update(float(respJSON["progress"]["completion"]))
                window["TIME/LAYER"].update("Progress: " + respJSON["progress"]["printTime"] + "/" + respJSON["progress"]["printTimeLeft"])
            else:
                window.Title = "No connection" # TODO Change this to notify the user that there is no job

        except requests.exceptions.ConnectionError as e:
            # Could not connect to api
            window.Title = "No connection"
    print("Close window")
    window.close()