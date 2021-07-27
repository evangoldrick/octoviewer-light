
def getKey(keyFile : str ="API-KEY.txt") -> str:
    with open(keyFile, "r") as keyReader:
        return str(keyReader.read().strip())