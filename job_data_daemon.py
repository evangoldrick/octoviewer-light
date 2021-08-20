import api_helper
import time
import threading

def noCallback():
    print("Default Callback")

def getData(apiHelper: api_helper.ApiHelper, url:str, callback:function):
    while True:
        time.sleep(1)
        apiHelper.parseResponseJson(apiHelper.getResponse(url))
