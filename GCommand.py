from dataclasses import dataclass

@dataclass
class GCommand:
    command: str
    parameters: dict
    byteCount: int
    layer: int

    def __init__(self, command: str, byteCount: int, layer: int = None):
        if command.startswith(";"):
            self.command = ";"
            self.parameters = dict({0:command[1:]})
        else:
            params = dict()
            for i in command.split(" "):
                params[i[0]] = float(i[1:])

            self.command = command.split(" ")[0]
            self.parameters = params
            
        self.byteCount = byteCount
        self.layer = layer


    def __eq__(self, o: object) -> bool:
        if isinstance(o, GCommand):
            if self.command == o.command and self.parameters == o.parameters and self.byteCount == o.byteCount and self.layer == o.layer:
                return True
        return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)

    def __lt__(self, o: object) -> bool:
        if isinstance(o, GCommand):
            if self.byteCount < o.byteCount:
                return True
            else:
                return False
        else:
            raise NotImplementedError(f"Cannot compare GCommand with {type(o)}")

    def __gt__(self, o: object) -> bool:
        if isinstance(o, GCommand):
            if self.byteCount > o.byteCount:
                return True
            else:
                return False
        else:
            raise NotImplementedError(f"Cannot compare GCommand with {type(o)}")

    def __le__(self, o: object) -> bool:
        if isinstance(o, GCommand):
            if self.byteCount <= o.byteCount:
                return True
            else:
                return False
        else:
            raise NotImplementedError(f"Cannot compare GCommand with {type(o)}")
    
    def __ge__(self, o: object) -> bool:
        if isinstance(o, GCommand):
            if self.byteCount >= o.byteCount:
                return True
            else:
                return False
        else:
            raise NotImplementedError(f"Cannot compare GCommand with {type(o)}")
    
    def isLayerLabel(self) -> bool:
        if self.command == ";" and self.parameters[0].startswith("LAYER:"):
            return True
        return False

    def getLayerLabel(self) -> int:
        if self.isLayerLabel():
            return int(self.parameters[0].split(":")[1])
        else:
            raise TypeError(f"This GCommand is not a layer comment {str(self)}")