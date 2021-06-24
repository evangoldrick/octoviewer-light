
def parse(fileName):
    with open(fileName, "rb") as gCodeFile:
        gCode = gCodeFile.read()
        print(gCode)

if __name__ == "__main__":
    parse()