import time
import requests

class ApiHelper:
    __lastRequestTime = 0
    rateLimitms = 1000

    def __updateTimer() -> None:
        ApiHelper.lastRequestTime = time.time_ns()

    def __millisecondsSinceLastRequest() -> None:
        return time.time_ns() - ApiHelper.__lastRequestTime

    def setRateLimit(rateTime:int) -> None:
        ApiHelper.rateLimitms = rateTime

    def getResponse(url : str, key : str) -> requests.Response:
        if ApiHelper.__millisecondsSinceLastRequest() > ApiHelper.rateLimitms:
            response = requests.get(url, headers={"X-Api-Key" : key})
        
            if response.status_code != 200:
                raise Exception('GET {} {}'.format(response.url, response.status_code))

            return response
        else:
            return None


if __name__ == "__main__":
    with open("API-KEY.md", "r") as keyFile:
        apiKey = keyFile.read().strip()
        print(ApiHelper.getResponse("http://octopi.local/api/job", apiKey).json())
    