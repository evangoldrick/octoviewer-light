# octoviewer-light
Shows data about an Octoprint (3D-Printing) job 
This program is meant to run on a Raspberry Pi 1

## Running the Program
1. You must have a octopi server running for the program to recieve data
1. Add a file called API-KEY.txt which contains an API key for the octopi server
1. The program can be run using the main.py or the run.sh file.
    1. main.py is preferred if running directly on device.
    1. run.sh is designed to be able to run the program from an ssh connection while allowing the UI to appear on the main monitor. In the future run.sh should also be able to detach itself from the ssh connection and run on the machine even after the user logs out.
    
## TODO
- [x] File Reading
- [x] Separating gcode into layers
- [ ] Interperating commands into actions
- [ ] REST API requests
    - [x] Get Job status
    - [ ] Get file name
    - [ ] Download gcode from octopi
- [ ] GUI
    - [x] Show print job info
    - [x] Progress bar
    - [ ] Draw gcode path
    - [ ] Lock layout

## What I Learned:
* How to interact with the Octoprint [REST API](https://docs.octoprint.org/en/master/api/index.html)
* Unit testing in python
* Parsing
* How to make a UI with SimpleGui
* Dataclasses in python
* Command line arguments; argv in python


## Resources
[Octoprint REST API](https://docs.octoprint.org/en/master/api/index.html)

[The PySimpleGUI Cookbook](https://pysimplegui.readthedocs.io/en/latest/cookbook/)