from GCommand import GCommand

def readAndCountGCode(fileName: str) -> list:
    with open(fileName, "rb") as gCodeFile:
        gCode = gCodeFile.readlines()
        byteCount = 0
        gCodeWithCounts = list()
        for line in gCode:
            gCodeWithCounts.append([line.decode('UTF-8').strip(), byteCount]) # Convert line to string and remove b'' from the lines, also add byte counts
            byteCount = byteCount + len(line)
        
        return gCodeWithCounts


def getLayerByComments(gCodeWithCounts: list):
    layerCount = 0
    layers = list()

    for line in gCodeWithCounts:
        if line[0].startswith(";Layer:"):
            layerCount = int(line[0].split(":")[1])

        while len(layers) <= layerCount:
            layers.append(list())
        layers[layerCount].append(line)
    
    return layers


def parseCommand(command: str) -> GCommand:
    temp = command.split(" ")[1:]
    params = dict()
    for i in temp:
        params[i[0]] = float(i[1:])

    return GCommand(command.split(" ")[0], )


def getParsedFile(fileName: str):
    return getLayerByComments(readAndCountGCode(fileName))


if __name__ == "__main__":
    with open("testOutput.txt", "w") as file:
        file.write(repr(getParsedFile("gCodeFiles/AI3M_70mm_SmallRod.gcode")))
    