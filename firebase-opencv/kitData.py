from opcua import Client, ua
from pyrebase import pyrebase  # firebase library
import time
from datetime import date, datetime


def fireinit():
    global db
    config = {
        'apiKey': "AIzaSyDPteYcsRi7Ym2vU0q1dQL31P90Mdo-L2A",
        'authDomain': "iafsmtraining-c08bd.firebaseapp.com",
        'databaseURL': "https://iafsmtraining-c08bd.firebaseio.com",
        'projectId': "iafsmtraining-c08bd",
        'storageBucket': "iafsmtraining-c08bd.appspot.com",
        'messagingSenderId': "940148611283",
        'appId': "1:940148611283:web:c32ad8fe8a48f145755c26"
    }

    firebasePyre = pyrebase.initialize_app(config)
    db = firebasePyre.database()


def connectNode(array):
    global nodes

    for i in range(len(array)):
        node = array[i]
        name = node['name']
        address = node['address']
        data = client.get_node(address)
        add = {'name': name, 'data': data}
        nodes.append(add)
    # print('initialised all nodes. use array - nodes', nodes)


def current_date():
    x = date.today().strftime("%d-%m-%Y")
    return x


def current_time():
    x = datetime.now().strftime("%H:%M:%S")
    return x


def check():
    global nodes

    while True:
        d = str(current_date())
        t = str(current_time())
        tS = d + " " + t
        client.connect()

        val = []
        for i in nodes:
            data = i["data"].get_value()
            val.append(data)
        print("testing if val stores current values of nodes", val)

        data = {'rfid': {'value': val[0], 'timeStamp': tS}, 'bodyHeight': {'value': val[1], 'timeStamp': tS},
                'circleDiameter': {'value': val[2], 'timeStamp': tS},
                'distanceStation': {'value': val[3], 'timeStamp': tS},
                'solenoidStation': {'value': val[4], 'timeStamp': tS},
                'cameraStation': {'value': val[5], 'timeStamp': tS},
                'rfidStation': {'value': val[6], 'timeStamp': tS}
                }
        db.child("kitdata").set(data)
        print('data pushed')

        client.disconnect()

        time.sleep(4)


if __name__ == "__main__":
    nodes = []
    db = ''
    fireinit()
    url = "opc.tcp://10.226.52.110:4990"
    client = Client(url)

    client.connect()
    print('connected')
    array = [{'name': 'rfid', 'address': 'ns=3;s=[train]RFID_Tagvalue'},
             {'name': 'bodyHeight', 'address': 'ns=3;s=[train]Body_Height'},
             {'name': 'circleDiameter', 'address': 'ns=3;s=[train]Circle_dia'},
             {'name': 'distanceStation',
                 'address': 'ns=3;s=[train]Distance_Station'},
             {'name': 'solenoidStation',
                 'address': 'ns=3;s=[train]Solenoid_station'},
             {'name': 'cameraStation',
                 'address': 'ns=3;s=[train]Camera_Station'},
             {'name': 'rfidStation', 'address': 'ns=3;s=[train]RFID_Station'}
             ]
    connectNode(array)

    client.disconnect()
    check()
else:
    print('idk')
