from g_command import GCommand

def readAndCountGCode(fileName: str) -> list:
    with open(fileName, "rb") as gCodeFile:
        gCode = gCodeFile.readlines()
        byteCount = 0
        gCodeWithCounts = list()

        for line in gCode:
            formattedLine = line.decode(encoding='UTF-8').strip() # Convert to string
            gCodeCommand = GCommand(formattedLine, byteCount)
            
            gCodeWithCounts.append(gCodeCommand) 
            byteCount = byteCount + len(line)
        
        return gCodeWithCounts


def getLayerByComments(gCodeWithCounts: list) -> list:
    currentLayer = 0
    layers = list()
    for line in gCodeWithCounts:
        if line.isLayerLabel():
            currentLayer = line.getLayerLabel()
        
        while len(layers) <= currentLayer:
            layers.append(list())

        line.layer = currentLayer
        layers[currentLayer].append(line)

    return layers

def getParsedFileByComments(fileName: str) -> list:
    return getLayerByComments(readAndCountGCode(fileName))
