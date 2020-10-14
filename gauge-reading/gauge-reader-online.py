import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import argparse
from pyrebase import pyrebase
import analog_gauge_reader as reader

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

def gauge_number():
    gauge_index = db.child("GaugeReading").get().val()['gaugeNumber'] 
    return gauge_index

def cvTrigger():
    a = db.child("GaugeReading").get().val()['trigger']
    return str(a)

def setTrigger():
    data = {'trigger':'True'}
    db.child("GaugeReading").update(data)

def setValue(val):
    data = {'reading':val}
    db.child("GaugeReading").update(data)

def imgDownload(path):
    path_on_cloud = str(db.child("GaugeReading").get().val()['imageName'])
    storage.child(path_on_cloud).download(path)

def main():
    fireinit()
    calibration_path = '/media/dev/Data1/transfer/IITDFSM/IITDTrialCodes/gauge-reading/gauge-details.csv'
    download_path = '/media/dev/Data1/transfer/IITDFSM/IITDTrialCodes/gauge-reading/images/downloaded.png'
    if cvTrigger() == "True":
        imgDownload(download_path)
        gauge_index = gauge_number()
        val,units = reader.cv(gauge_index,download_path,calibration_path)
        print('Reading of the gauge: ',val,' ',units)
        setValue(val)
        setTrigger() 
    

if __name__=='__main__':
    main()
   	
