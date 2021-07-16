
from array import array


def readAndCountGCode(fileName) -> array:
    with open(fileName, "rb") as gCodeFile:
        gCode = gCodeFile.readlines()
        byteCount = 0
        gCodeWithCounts = list()
        for line in gCode:
            gCodeWithCounts.append([byteCount, str(line.strip())[2:-1]]) # Convert line to string and remove b'' from the lines, also add byte counts
            byteCount = byteCount + len(line)
        
        return gCodeWithCounts

if __name__ == "__main__":
    print(readAndCountGCode("gCodeFiles/AI3M_70mm_SmallRod.gcode")[0][1])
    