from opcua import Client
import time
import ClientNodes as c
import rough as errorCheck
def power():
    k = True
    while k == True:
        v = input("Power (on/off): ")
        if (v.lower()=='on'):
            power= True
            c.Power.set_value(power)
            print('Power On: ', power )
            pallet()
            k = False
        elif v.lower() =='off':
            power= False
            c.Power.set_value(power)
            print('Power On: ', power )
            k = True
        else:
            print("Only on or off allowed as input \n")    
            k= True      

def pallet():
    k = True
    while k == True:
        p = input("Pallet Placed (yes/no): ")
        if (p.lower()=='yes'):
            pallet= True
            c.Pallet.set_value(pallet)
            
            time.sleep(1)
            
            k= False
            order()
        elif p.lower() =='no':
            pallet= False
            c.Pallet.set_value(pallet)
            k = True
        else:
            print("Only yes or no allowed as input \n")    
            k= True

def order():
    k = True
    while k == True:
        o = input("Place order (yes/no): ")
        if o.lower() =='yes':
            order_Status= True
            k = False
        elif o.lower() =='no':
            order_Status= False
            k = True
        else:
            print("Only yes or no allowed as input")    
            k= True
    c.Order_Status.set_value(order_Status)

class SubHandler(object):
    def datachange_notification(self, node, val, data):
        tagList = []
        for i in c.tagListInt:
            tagList.append(i.get_value())
            #tagList.append(1)
        tagBoolVals = list(map(bool,tagList))
        errorCheck.faults(tagBoolVals)

        if node == c.Entry_Sensor:
            if val == 1:
                print('Entry Sensor: Pallet placed \n')

        elif node == c.Order_Status:
            if val == True:
                print('Order Status: Order Received \n')

        elif node == c.Stopper:
            if val == 1:
                print('Stopper: Up \n')
            elif val == 2:
                print('Stopper: Down \n')

        elif node == c.Conveyor:
            if val == 1:
                print('Conveyor: Started \n')
            elif val == 2:
                print('Conveyor: Stopped \n')

        elif node == c.Intermediate_Sensor:
            if val == 1:
                print('Pallet crossed Intermediate Sensor successfully \n')
            
        elif node == c.Operational_Sensor:
            if val == 1:
                print('Pallet is at Operational Sensor \n')
        
        elif node == c.Bottom_Cylinder:
            if val == 1:
                print('Bottom cylinder: Pallet Clamped \n')
            elif val == 2:
                print('Bottom cylinder: Pallet Unclamped \n')
                   
        elif node == c.Clamping_Cylinder:
            if val == 1:
                print('Clamping cylinder: Pulled out \n')

        elif node == c.RFID_reader:
            if val == 1:
                print ('RFID reader reads RFID tag \n')

        elif node == c.Gripper:
            if val == 1:
                print('Gripper picks the valve body from tray \n')
                print('Valve body placed in the pallet \n')
            elif val == 2:
                print("Gripper places the valve body on rejection tray \n")
                print('Next valve body is to be picked up \n')

        elif node == c.Vision_Sensor:
            if val == 1:
                print('Gripper is adjusted to align the vision sensor to the valve body \n')
           
        elif node == c.Motor:
            if val == 1: 
                print('Motor engages with the pallet \n')
            elif val == 2:
                print('Motor Stopped \n')

        elif node == c.Lever:
            if val == 1:
                print('Lever is pushed down for rotation \n')
            elif val == 2:
                print('Lever is pushed up \n')

        elif node == c.Rotation:
            if val == 1:
                print('Valve body is rotated by 90 degree \n')

        elif node == c.Face1:
            if val == 1:
                print('Face 1 scanned \n')

        elif node == c.Face2:
            if val == 1:
                print('Face 2 scanned \n')

        elif node == c.Face3:
            if val == 1:
                print('Face 3 scanned \n')

        elif node == c.Face4:
            if val == 1:
                print('Face 4 scanned \n')

        elif node == c.Profile_Status:
            if val == '1':
                print('Profile Matched \n')
        
        elif node == c.Pallet:
            if val == False:
                print('Pallet is at exit \n')

        elif node == c.Exit_Sensor:
            if val == 1:                
                print('Exit \n')

        elif node == c.Rejection:
            if val == 1:
                print('Profile Not Matched \n')
                print('Profile Rejected \n')
                

url = "opc.tcp://localhost:61032"
client = Client(url)

try:
    client.connect()
    print("Client Connected \n") 

    sub = client.create_subscription(500, SubHandler())
    
    handle = sub.subscribe_data_change(c.Pallet)
    handle = sub.subscribe_data_change(c.Entry_Sensor)
    handle = sub.subscribe_data_change(c.Order_Status)
    handle = sub.subscribe_data_change(c.Stopper)
    handle = sub.subscribe_data_change(c.Conveyor)
    handle = sub.subscribe_data_change(c.Intermediate_Sensor)
    handle = sub.subscribe_data_change(c.Operational_Sensor)   
    handle = sub.subscribe_data_change(c.Bottom_Cylinder)
    handle = sub.subscribe_data_change(c.Clamping_Cylinder)
    handle = sub.subscribe_data_change(c.RFID_reader)
    handle = sub.subscribe_data_change(c.Gripper)
    handle = sub.subscribe_data_change(c.Vision_Sensor)
    handle = sub.subscribe_data_change(c.Motor)
    handle = sub.subscribe_data_change(c.Lever)
    handle = sub.subscribe_data_change(c.Rotation)
    handle = sub.subscribe_data_change(c.Face1)
    handle = sub.subscribe_data_change(c.Face2)
    handle = sub.subscribe_data_change(c.Face3)
    handle = sub.subscribe_data_change(c.Face4)
    handle = sub.subscribe_data_change(c.Profile_Status) 
    handle = sub.subscribe_data_change(c.Pallet)    
    handle = sub.subscribe_data_change(c.Exit_Sensor)
    handle = sub.subscribe_data_change(c.Rejection)

    power()
    
except:
    print("")

     
           
       
 
