
def getKey(keyFile : str ="API-KEY.md") -> str:
    with open(keyFile, "r") as keyReader:
        return str(keyReader.read().strip())