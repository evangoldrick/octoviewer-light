import time
import requests
import json

from requests.models import Response
import key_reader
class ApiHelper:
    __lastRequestTime:int
    rateLimitms:int

    def __init__(self, rateLimitms=1000) -> None:
        self.__lastRequestTime = 0
        self.rateLimitms = rateLimitms
        self.key = key_reader.getKey()

    def __updateTimer(self) -> None:
        lastRequestTime = time.time_ns()

    def __millisecondsSinceLastRequest(self) -> None:
        return time.time_ns() - self.__lastRequestTime

    def setRateLimit(self, rateTime:int) -> None:
        rateLimitms = rateTime

    def getRateLimit(self) -> int:
        return self.rateLimitms

    def getResponse(self, url : str, key : str = None) -> requests.Response:
        if key is None:
            key = self.key
        if self.__millisecondsSinceLastRequest() < self.rateLimitms:
            raise RateLimitError()
        
        response = requests.get(url, headers={"X-Api-Key" : key})
    
        if response.status_code != 200:
            raise requests.RequestException('GET {} {}'.format(response.url, response.status_code))
            
        return response

    def parseResponseJson(self, response:requests.Response) -> list:
        x = json.loads(response.json)
        print(x)
        

class RateLimitError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

