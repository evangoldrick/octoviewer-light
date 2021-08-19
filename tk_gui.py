import api_helper
import key_reader

import requests
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        
        self.create_widgets()

    def create_widgets(self):
        self.gcodeGraph = tk.Label(self, text="graph goes here")

        self.hi_there = tk.Button(self, text="Manual request", command=api_helper.ApiHelper.getResponse)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        

    def say_hi(self):
        print("hi there, everyone!")


def start():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    start()

