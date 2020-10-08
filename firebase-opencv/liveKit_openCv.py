from opcua import Client, ua
from pyrebase import pyrebase # firebase library
import time
from datetime import date, datetime 
import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt
from cv2 import cv2

def fireinit():
    global db, storage
    config = {
        'apiKey': "AIzaSyCGOKhfIzz84YH4N3BesWNUCJ7TMZrrLCI",
        'authDomain': "iotc2020-41f98.firebaseapp.com",
        'databaseURL': "https://iotc2020-41f98.firebaseio.com",
        'projectId': "iotc2020-41f98",
        'storageBucket': "iotc2020-41f98.appspot.com",
        'messagingSenderId': "92339853452",
        'appId': "1:92339853452:web:bb90e76f6362ede61603a9",
        'measurementId': "G-RS1ZFQ23J9"
    }

    firebasePyre = pyrebase.initialize_app(config)
    storage = firebasePyre.storage()
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
    x = date.today().strftime("%Y-%m-%d")
    return x

def current_time():
    x = datetime.now().strftime("%H:%M:%S")
    return x

def cv():

    image = cv2.imread("downloaded.png")
    image=cv2.resize(image, dsize=(600, 900))

    # image2 = cv2.imread("Green1.jpg")
    # image2=cv2.resize(image2, dsize=(600, 900))

    b,g,r = cv2.split(image)       # get b,g,r
    rgb_img = cv2.merge([r,g,b])

    lower_red=np.array([235,195,197])
    upper_red=np.array([255,220,230])

    mask=cv2.inRange(rgb_img,lower_red,upper_red)
    result = cv2.bitwise_and(image, image, mask = mask)
    print(result.shape)

    cropped = result[0:200, 0:200]
    plt.imshow(cropped)
    cropped=cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    y=pd.DataFrame(cropped)
    a=1
    for i in range(200):
        for j in range(200):
            if(y[i][j]!=0):
                a=2
                print(y[i][j])
                
    print('opencv result is -', a)           
    if a == 1:
        print("No error")
        e = {"checked": "True", "error": "1"} 
    else:
        print('Error')
        e = {"checked": "True", "error": "2"}
    db.child("FSMKit1").child("errorDetection").update(e)

def cvTrigger():
    a = db.child("FSMKit1").child("errorDetection").get().val()['checked']
    return str(a)

def imgDownload():
    
    path_on_cloud = str(db.child("FSMKit1").child("errorDetection").get().val()['imageName'])
    storage.child(path_on_cloud).download('downloaded.png')

def check():
    global nodes
    n = 1

    while True:
        date = str(current_date())
        t = str(current_time())

        client.connect()

        val =  []
        for i in nodes:
            data = i["data"].get_value()
            val.append(data)
        print("testing is val stores current values of nodes", val)

        if val[0] == 0:
            dsconn = {'connection' : 'not connected'}    
        else:
            dsconn = {'connection' : 'connected'}
        db.child("FSMKit1").child('distanceSensor').set(dsconn)
        ioconn = {'I1' : '0', 'I2' : '0'}
        if any(val[6:]):
            ioconn = {'I1' : '0', 'I2' : '1'}
        elif val[5]:
            ioconn = {'I1' : '1', 'I2' : '0'}
        db.child("FSMKit1").child('PortInsertion').set(ioconn)

        vS = {
            'v1': 100*val[1],
            'v2': 100*val[2],
            'v3': 100*val[3],
            'v4': 100*val[4]
        }
        db.child("FSMKit1").child('vibrationSensor').child(date).child(t).update(vS)
        print('run - ', n)
        n += 1

        client.disconnect()

        if cvTrigger() == "False":
            imgDownload()
            cv() 

        time.sleep(4)

if __name__ == "__main__":
    nodes = []
    db = ''
    storage = ''
    fireinit()
    url = "opc.tcp://192.168.0.7:4990"
    client = Client(url)

    client.connect()
    print('connected')
    array = [{'name': 'distanceSensor', 'address': 'ns=3;s=::[Kit1]iol:I.Data[90]'},
            {'name': 'vibrationSensor1', 'address': 'ns=3;s=::[Kit1]v:I1.Data[0]'},
            {'name': 'vibrationSensor2', 'address': 'ns=3;s=::[Kit1]v:I1.Data[1]'},
            {'name': 'vibrationSensor3', 'address': 'ns=3;s=::[Kit1]v:I1.Data[2]'},
            {'name': 'vibrationSensor4', 'address': 'ns=3;s=::[Kit1]v:I1.Data[3]'},
            {'name': 'ioOne', 'address': 'ns=3;s=[Kit1]I1'}, 
            {'name': 'ioTwo', 'address': 'ns=3;s=[Kit1]I2'},
            {'name': 'ioThree', 'address': 'ns=3;s=[Kit1]I3'},
            {'name': 'ioFour', 'address': 'ns=3;s=[Kit1]I4'},
            {'name': 'ioFive', 'address': 'ns=3;s=[Kit1]I5'},
            {'name': 'ioSix', 'address': 'ns=3;s=[Kit1]I6'},
            {'name': 'ioSeven', 'address': 'ns=3;s=[Kit1]I7'},
            {'name': 'ioEight', 'address': 'ns=3;s=[Kit1]I8'},
            {'name': 'ioNine', 'address': 'ns=3;s=[Kit1]I9'},
            {'name': 'ioTen', 'address': 'ns=3;s=[Kit1]I10'},
            {'name': 'ioEleven', 'address': 'ns=3;s=[Kit1]I11'},
            {'name': 'ioTwelve', 'address': 'ns=3;s=[Kit1]I12'}]
    connectNode(array)

    client.disconnect()
    check()
else:
    print('idk')