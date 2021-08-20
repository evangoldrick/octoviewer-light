import api_helper
import time
import threading
class JobDaemon:

    def __init__(self):
        self.daemon = threading.Thread(target=self.getData)
        self.functions = []
        self.stayAlive = True
        
    def start(self):
        self.daemon.start()
    
    def stop(self):
        self.stayAlive = False
        self.daemon.join(timeout=10)

    def addFunction(self, func, *args, **kwargs):
        self.functions.append((func, args, kwargs))

    def getData(self):
        while self.stayAlive:
            for func in self.functions:
                func[0](*(func[1]), **(func[2]))
            time.sleep(1)
            
            
