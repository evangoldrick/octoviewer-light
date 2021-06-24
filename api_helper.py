import requests


def getResponse(url : str, key : str) -> requests.Response:

    response = requests.get(url, headers={"X-Api-Key" : key})

    if response.status_code != 200:
        raise Exception('GET {} {}'.format(response.url, response.status_code))

    return response


if __name__ == "__main__":
    with open("API-KEY.md", "r") as keyFile:
        apiKey = keyFile.read().strip()
        print(getResponse("http://octopi.local/api/job", apiKey).json())
    