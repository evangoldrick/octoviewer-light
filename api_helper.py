import time
import requests

class Timer:
    lastRequest = 0

    def update():
        Timer.lastRequest = time.time_ns()

    def compareSeconds(delay):
        if (Timer.lastRequest/1000) + delay < time.time_ns():
            return True
        return False

    def compareNanoseconds(delayNS):
        if Timer.lastRequest + delayNS < time.time_ns():
            return True
        return False

def getResponse(url : str, key : str) -> requests.Response:
    if Timer.compareSeconds(1):
        response = requests.get(url, headers={"X-Api-Key" : key})
    
        if response.status_code != 200:
            raise Exception('GET {} {}'.format(response.url, response.status_code))

        return response
    else:
        return None


if __name__ == "__main__":
    with open("API-KEY.md", "r") as keyFile:
        apiKey = keyFile.read().strip()
        print(getResponse("http://octopi.local/api/job", apiKey).json())
    