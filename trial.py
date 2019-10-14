import requests
import json
import time




while True:
    url = requests.get("https://borrowifi-7bea2.firebaseio.com/Members.json")
    r = url.json()
    print(r)
    time.sleep(1)