import json
from urllib.request import urlopen

def getResponse(ipAddres):
    response = urlopen("https://freegeoip.app/json/"+ipAddres).read().decode('utf-8')
    return response

def getCountry(ipAddres):
    response = getResponse(ipAddres)
    responseJson = json.loads(response)
    return responseJson.get("country_name")

def getRegionName(ipAddres):
    response = getResponse(ipAddres)
    responseJson = json.loads(response)
    return responseJson.get("region_name")

def getCity(ipAddres):
    response = getResponse(ipAddres)
    responseJson = json.loads(response)
    return responseJson.get("city")

ipAddres = input("Type your IPAdress: ")
print(getCountry(ipAddres))
print(getRegionName(ipAddres))
print(getCity(ipAddres))
