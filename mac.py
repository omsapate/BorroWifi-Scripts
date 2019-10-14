import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

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
    print(macid)
    print(timer)

    



    #print(macid.keys())  # new data at /reference/event.path. None if deleted

firebase_admin.db.reference('Members').listen(listener)