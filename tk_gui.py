import api_helper
import job_data_thread

import tkinter as tk
from tkinter import ttk
import matplotlib
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure


class GraphFrame(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(borderwidth=2, relief="groove")
        self.create_widgets()

    def create_widgets(self):
        self.fig = Figure(figsize=(6, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.updatePlot([(1, 1), (3, 1), (2, 3), (3, 3)])
        self.ax.autoscale_view()
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().pack(side="left")

    def updatePlot(self, vertices: list) -> None:
        self.ax.add_patch(self.createPatchPath(vertices))

    def update3DPlot(self) -> None:
        pass
        # TODO add 3d plots

    def createPatchPath(self, vertices: list, color: str = "black") -> PathPatch:
        if len(vertices) <= 1:
            raise ValueError(f"The vertices list should have at least two vertecies. You provdied only {len(vertices)}, {vertices}")
        codes = [Path.MOVETO] + [Path.LINETO] * (len(vertices)-1)

        path = matplotlib.path.Path(vertices, codes)
        return PathPatch(path, facecolor="None", edgecolor=color)

    def say_hi(self):
        print("hi there, everyone!")


class InfoFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(borderwidth=2, relief="sunken")
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.infoLabels = dict()
        self.defaultInfoLabels = ["fileName", "jobPercentage", "x"]

        for lab in self.defaultInfoLabels:
            self.infoLabels[lab] = tk.Label(self, text=lab, font=("Arial", 30), borderwidth=2, relief="groove", pady=10)

        for i, lab in enumerate(self.infoLabels.keys()):
            self.rowconfigure(i, weight=1)
            self.infoLabels[lab].grid(row=i, column=1, sticky="NE")

        self.requestButton = tk.Button(self, text="Manual request", command=self.requestPrintInfo)
        self.requestButton.grid(row=len(self.defaultInfoLabels)+1, column=1, pady=5, sticky="S")

        self.quitButton = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quitButton.grid(row=len(self.defaultInfoLabels)+2, column=1, pady=5, sticky="S")

        self.progressBar = ttk.Progressbar(self, value=100, maximum=100, orient="vertical")
        self.progressBar.grid(row=0, column=0, rowspan=len(self.infoLabels), sticky="NWS")

    def requestPrintInfo(self):
        self.master.apiHelper.getResponse("http://octopi.local/api/job")

    def say_hi(self):
        print("hi there, everyone!")

    def setDefaultJobStatus(self):
        self.fileName["text"] = "No Connection"
        self.jobPercentage["text"] = "0%"
        
def start():
    root = tk.Tk()
    root.title("octoviewer-light")
    root.geometry("1400x800")
    root.apiHelper = api_helper.ApiHelper()
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    graph = GraphFrame(master=root)
    graph.grid(row=0, column=0, sticky="NESW")
    
    info = InfoFrame(master=root)
    info.grid(row=0, column=1, sticky="NESW")

    requestsThread = job_data_thread.JobDaemon()
    root.mainloop()


if __name__ == "__main__":
    start()
