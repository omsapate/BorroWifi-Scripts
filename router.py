from requests import get
from base64 import b64encode
from urllib.parse import quote
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

######################################################################################
# constants
tplink = '192.168.0.1'
user = 'admin'
password = 'admin'

# constants for modification of records

url_template_for_adding_mac_id = 'http://{}/userRpm/LanMacFilterRpm.htm?'  #pass paramaters for adding user mac id
url_template_for_deleting_mac_id = 'http://{}/userRpm/LanMacFilterRpm.htm?Del='  #pass id of rule to delete it

######################################################################################
#constants for addind mac id received from the user
Mac="20-k0-98-72-40-7c"
Desc="pythontesting"
State=1
Changed=0
SelIndex=0
Page=1
Save="Save"
Delete=0

#############################################################################

if __name__ == '__main__':
    auth_bytes = bytes(user+':'+password, 'utf-8')
    auth_b64_bytes = b64encode(auth_bytes)
    auth_b64_str = str(auth_b64_bytes, 'utf-8')

    auth_str = quote('Basic {}'.format(auth_b64_str))

    auth = {
    'Referer': 'http://'+tplink+'/', 
    'Authorization': auth_str,
    }

    

def addMacAddress(Mac):
    add_mac = ("{}Mac={}&Desc={}&State={}&Changed={}&Se1Index={}&Page={}&Save={}".format(url_template_for_adding_mac_id,Mac,Desc,State,Changed,SelIndex,Page,Save))
    add_mac_id = add_mac.format(tplink)
    r = get(add_mac_id, headers=auth)


# Fetch the service account key JSON file contents
cred = credentials.Certificate('key.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://borrowifi-7bea2.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('/Members')

def listener(event):
    #print(event.event_type)  # can be 'put' or 'patch'
    macid = event.path  #string
    timer = str(event.data)  #dictionary
    print(timer)

    if "/" in macid:
        newmacid=macid.replace("/","").replace(":","-")
        print(newmacid)
        addMacAddress(newmacid)
    #print(macid.keys())  # new data at /reference/event.path. None if deleted

firebase_admin.db.reference('Members').listen(listener)
  

############################################################################

# generating authentication token and referrers for script authentication and modification

######################################################################
    

   
#def deleteMacAddress(Mac):
#    delete_mac =("{}{}".format(url_template_for_deleting_mac_id,Delete))
#    delete_mac_id = delete_mac.format(tplink)
#    r = get(delete_mac_id, headers=auth)

########################################################################

