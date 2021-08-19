import time
import requests

class ApiHelper:
    __lastRequestTime:int
    rateLimitms:int

    def __init__(self, rateLimitms=1000) -> None:
        self.rateLimitms = rateLimitms

    def __updateTimer(self) -> None:
        lastRequestTime = time.time_ns()

    def __millisecondsSinceLastRequest(self) -> None:
        return time.time_ns() - self.__lastRequestTime

    def setRateLimit(self, rateTime:int) -> None:
        rateLimitms = rateTime

    def getRateLimit(self) -> int:
        return self.rateLimitms

    def getResponse(self, url : str, key : str) -> requests.Response:
        if self.__millisecondsSinceLastRequest() > self.rateLimitms:
            response = requests.get(url, headers={"X-Api-Key" : key})
        
            if response.status_code != 200:
                raise requests.RequestException('GET {} {}'.format(response.url, response.status_code))
                
            return response
        else:
            return None
