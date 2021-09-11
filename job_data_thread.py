import api_helper
import time
import threading
class RepeatJobThread:
    def __init__(self, repeatTime=1):
        self.process = threading.Thread(target=self.runFunctions)
        self.functions = []
        self.stayAlive = True
        self.repeatTime = repeatTime
        
    def setRepeatTime(self, newTime:int) -> None:
        self.repeatTime = newTime

    def start(self):
        self.process.start()
    
    def stop(self) -> None:
        self.stayAlive = False
        self.process.join(timeout=10)

    def addFunction(self, func, *args, **kwargs) -> None:
        self.functions.append((func, args, kwargs))

    def runFunctions(self) -> None:
        while self.stayAlive:
            for func in self.functions:
                func[0](*(func[1]), **(func[2]))
            time.sleep(self.repeatTime)


