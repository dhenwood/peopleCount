import requests
import os
import xmltodict
from base64 import b64encode


# Replace following two lines to your endpoints username and password
username = os.environ.get("TP_USERNAME")
password = os.environ.get("TP_PASSWORD")

authTokenBytes = b64encode(bytes(username + ':' + password, "utf-8"))
authToken = authTokenBytes.decode('utf-8')


def getPeopleCount():

    fqdnEndpoint = "roomkit.example.com"
    url = "http://%s/status.xml" % fqdnEndpoint


    headers = {"Accept": "text/xml",
           "Authorization": "Basic %s" % authToken
           }

    resp = requests.get(url, headers=headers)

    if(resp.status_code == 200):
        xmlData = xmltodict.parse(resp.text)
        peopleCount = xmlData['Status']['RoomAnalytics']['PeopleCount']['Current']
        print("Current people count: ",peopleCount)
    
    else:
        print("Error occured with status code: ",resp.status_code)
    


if __name__ == '__main__':
    getPeopleCount()
    
