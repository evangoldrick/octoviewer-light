import time
import requests


__lastRequestTime = 0
rateLimitms = 1000

def __updateTimer() -> None:
    lastRequestTime = time.time_ns()

def __millisecondsSinceLastRequest() -> None:
    return time.time_ns() - __lastRequestTime

def setRateLimit(rateTime:int) -> None:
    rateLimitms = rateTime

def getResponse(url : str, key : str) -> requests.Response:
    if __millisecondsSinceLastRequest() > rateLimitms:
        response = requests.get(url, headers={"X-Api-Key" : key})
    
        if response.status_code != 200:
            raise requests.RequestException('GET {} {}'.format(response.url, response.status_code))
            
        return response
    else:
        return None


if __name__ == "__main__":
    with open("API-KEY.md", "r") as keyFile:
        apiKey = keyFile.read().strip()
        print(getResponse("http://octopi.local/api/job", apiKey).json())
    