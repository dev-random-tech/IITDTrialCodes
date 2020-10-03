from opcua import Server
import time
from random import randint
import ServerNodes as s

def entrySensorError(): 
    Ent_IO_DataValidity = randint(0,1)
    s.ent_IO_DataValidity.set_value(Ent_IO_DataValidity)

    Ent_diag1_IO1 = randint(0,1)
    s.ent_diag1_IO1.set_value(Ent_diag1_IO1)

    Ent_diag1_IO2 = randint(0,1)
    s.ent_diag1_IO2.set_value(Ent_diag1_IO2)

    Ent_diag1_IO3 = randint(0,1)
    s.ent_diag1_IO3.set_value(Ent_diag1_IO3)
    
    Ent_diag1_IO4 = randint(0,1)
    s.ent_diag1_IO4.set_value(Ent_diag1_IO4)
    
    Ent_diag1_IO5 = randint(0,1)
    s.ent_diag1_IO5.set_value(Ent_diag1_IO5)

    Ent_diag1_IO6 = randint(0,1)
    s.ent_diag1_IO6.set_value(Ent_diag1_IO6)
    
    Ent_diag1_IO7 = randint(0,1)
    s.ent_diag1_IO7.set_value(Ent_diag1_IO7)
    
    Ent_diag2_IO1 = randint(0,1)
    s.ent_diag2_IO1.set_value(Ent_diag2_IO1)
    
    Ent_diag2_IO2 = randint(0,1)
    s.ent_diag2_IO2.set_value(Ent_diag2_IO2)

    Ent_diag2_IO3 = randint(0,1)
    s.ent_diag2_IO3.set_value(Ent_diag2_IO3)

    Ent_PowerSupply = randint(0,1)
    s.ent_PowerSupply.set_value(Ent_PowerSupply)
    
    Ent_DigitalOutput = randint(0,1)
    s.ent_DigitalOutput.set_value(Ent_DigitalOutput)
    
    Ent_IO_DeviceError = randint(0,1)
    s.ent_IO_DeviceError.set_value(Ent_IO_DeviceError)

    Ent_IO_DeviceWarning = randint(0,1)    
    s.ent_IO_DeviceWarning.set_value(Ent_IO_DeviceWarning)

    Ent_IO_DeviceNotification = randint(0,1)
    s.ent_IO_DeviceNotification.set_value(Ent_IO_DeviceNotification)
    
def intermediateSensorError(): 
    Int_IO_DataValidity = randint(0,1)
    s.int_IO_DataValidity.set_value(Int_IO_DataValidity)
    
    Int_diag1_IO1 = randint(0,1)
    s.int_diag1_IO1.set_value(Int_diag1_IO1)
    
    Int_diag1_IO2 = randint(0,1)
    s.int_diag1_IO2.set_value(Int_diag1_IO2)
    
    Int_diag1_IO3 = randint(0,1)
    s.int_diag1_IO3.set_value(Int_diag1_IO3)
    
    Int_diag1_IO4 = randint(0,1)
    s.int_diag1_IO4.set_value(Int_diag1_IO4)

    Int_diag1_IO5 = randint(0,1)
    s.int_diag1_IO5.set_value(Int_diag1_IO5)

    Int_diag1_IO6 = randint(0,1)
    s.int_diag1_IO6.set_value(Int_diag1_IO6)
    
    Int_diag1_IO7 = randint(0,1)
    s.int_diag1_IO7.set_value(Int_diag1_IO7)
    
    Int_diag2_IO1 = randint(0,1)
    s.int_diag2_IO1.set_value(Int_diag2_IO1)
    
    Int_diag2_IO2 = randint(0,1)
    s.int_diag2_IO2.set_value(Int_diag2_IO2)
    
    Int_diag2_IO3 = randint(0,1)
    s.int_diag2_IO3.set_value(Int_diag2_IO3)
    
    Int_PowerSupply = randint(0,1)
    s.int_PowerSupply.set_value(Int_PowerSupply)
    
    Int_DigitalOutput = randint(0,1)
    s.int_DigitalOutput.set_value(Int_DigitalOutput)

    Int_IO_DeviceError = randint(0,1)
    s.int_IO_DeviceError.set_value(Int_IO_DeviceError)

    Int_IO_DeviceWarning = randint(0,1)
    s.int_IO_DeviceWarning.set_value(Int_IO_DeviceWarning)

    Int_IO_DeviceNotification = randint(0,1)
    s.int_IO_DeviceNotification.set_value(Int_IO_DeviceNotification)

    
    

def operation():

    # Once it is read that the body is 5 by 2 or 3 by 2,
    # accordingly gripper will pick the particular valve body from tray and place it in the pallet.
    gripper = 1
    s.Gripper.set_value(gripper)
    print('Gripper picks the valve body from tray \n')
    print('Valve body placed in the pallet \n')
    time.sleep(1)

    #entrySensorError()
    intermediateSensorError() 
    # Once clamping is done, gripper moves where the visions will be focused towards the valve body.
    # Gripper is adjusted to align the vision sensor to the valve body
    vision_Sensor = 1
    s.Vision_Sensor.set_value(vision_Sensor)
    print('Gripper is adjusted to align the vision sensor to the valve body \n')
    time.sleep(1)

    # Motor engages with the pallet
    motor = 1
    s.Motor.set_value(motor)
    print('Motor engages with the pallet \n')
    time.sleep(1)

    # Lever is pushed down for rotation
    lever = 1
    s.Lever.set_value(lever)
    print('Lever is pushed down for rotation \n')
    time.sleep(1)

    # Using motor, valve body is rotated by 90 degree
    rotation = 1
    s.Rotation.set_value(rotation)
    print('Valve body is rotated by 90 degree \n')
    time.sleep(2)

    #Profile is captured
    print('Face 1 is being scanned \n')
    time.sleep(3)
    face1 = 1
    s.Face1.set_value(face1)


    print('Face 2 is being scanned \n')
    time.sleep(3)
    face2 = 1
    s.Face2.set_value(face2)

    print('Face 3 is being scanned \n')
    time.sleep(3)
    face3 = 1
    s.Face3.set_value(face3)

    print('Face 4 is being scanned \n')
    time.sleep(3)
    face4 = 1
    s.Face4.set_value(face4)

    
    k = True
    while k == True:
        profile_Status = input("Enter 1 to accept the product and 0 to reject it: ")
        s.Profile_Status.set_value(profile_Status)
        #Once profile is correct, pallet will be disengaged from the operational sensor area and exit
        if profile_Status == '1':
            print('Profile Matched \n')
            time.sleep(1)
            print('Product Accepted \n')
            time.sleep(1)
            motor = 2
            s.Motor.set_value(motor)
            print('Motor Stopped \n')
            time.sleep(1)
            lever = 2
            s.Lever.set_value(lever)
            print('Lever is pushed up \n')
            time.sleep(1)
            stopper = 2
            s.Stopper.set_value(stopper)
            print('Stopper: Down \n')
            time.sleep(1)
            bottom_Cylinder = 2
            s.Bottom_Cylinder.set_value(bottom_Cylinder)
            print('Bottom Cylinder: Pallet Unclamped \n')
            time.sleep(1)
            conveyor = 1
            s.Conveyor.set_value(conveyor)
            print('Conveyor: Started \n')
            time.sleep(1)
            pallet= False
            s.Pallet.set_value(pallet)
            print('Pallet is at exit \n')
            time.sleep(1)
            conveyor = 2
            s.Conveyor.set_value(conveyor)
            print('Conveyor: Stopped \n')
            time.sleep(2)
            exit_Sensor = 1
            s.Exit_Sensor.set_value(exit_Sensor)
            print('Exit \n')
            k = False

        #If profile does not match with the standard one, then clamping cylinder retracts and gripper takes the valve body from pallet and rejects it and places it in the rejection area.
        elif profile_Status == '0':
            rejection = 1
            s.Rejection.set_value(rejection)
            print('Profile Not Matched \n')
            print('Product Rejected \n')
           
            gripper = 2
            s.Gripper.set_value(gripper)
            print("Gripper places the valve body on rejection tray \n")
            vision_Sensor = 0
            s.Vision_Sensor.set_value(vision_Sensor)
            motor = 0
            s.Motor.set_value(motor)
            lever = 0
            s.Lever.set_value(lever)    
            rotation = 0
            s.Rotation.set_value(rotation)
            face1 = 0
            s.Face1.set_value(face1)    
            face2 = 0
            s.Face2.set_value(face2)
            face3 = 0
            s.Face3.set_value(face3)
            face4 = 0
            s.Face4.set_value(face4)
            profile_Status = '0'
            s.Profile_Status.set_value(profile_Status)   
            exit_Sensor = 0
            s.Exit_Sensor.set_value(exit_Sensor)
            rejection = 0
            s.Rejection.set_value(rejection)
            print('Next valve body is to be picked up \n') 
            time.sleep(1)    

            operation()
            k = False
        
        else:
            
            print("Only 1 or 0 allowed as input")    
            k= True 

def main():
    # Power is switched on.
    print('Waiting for the status of power \n')
    while True:
        power = s.Power.get_value()
        if (power == True):
            break
    print('Power On: ', power, '\n')
    # Pallet placed in the entry sensor
    print('Waiting for the status of pallet \n')
    while True:
        pallet = s.Pallet.get_value()
        if (pallet == True):
            entry_Sensor = 1
            s.Entry_Sensor.set_value(entry_Sensor)
            print ('Entry Sensor: Pallet Placed \n')
            break  
    # Order is placed through app
    
    print('Waiting for order \n')
    while True:
        order_Status = s.Order_Status.get_value()
        if (order_Status == True):
            break
    print('Order Status: Order Received \n')
    #entrySensorError()
    #intermediateSensorError()
    # Stopper will be in the up position
    stopper = 1
    s.Stopper.set_value(stopper)
    print('Stopper: Up \n')

    # Conveyor gets started
    conveyor = 1
    s.Conveyor.set_value(conveyor)
    entry_Sensor =0
    print('Conveyor: Started \n')
    time.sleep(3)
    # Pallet will be moving towards operational sensor

    # In between entry sensor and operational sensor, there is intermediate sensor
    # All these are proximity sensors

    # Intermediate sensor checks pallet is moving or not
    intermediate_Sensor = 1
    s.Intermediate_Sensor.set_value(intermediate_Sensor)
    print('Pallet crossed Intermediate Sensor successfully \n')
    time.sleep(3)

    operational_Sensor = 1
    s.Operational_Sensor.set_value(operational_Sensor)
    print('Pallet is at Operational Sensor \n')

    # Once pallet reaches operational sensor, conveyor stops.
    conveyor = 2
    s.Conveyor.set_value(conveyor)
    print ('Conveyor: Stopped \n')

    # Now pneumatic part comes in – to engage pallet from the bottom,
    # pull the pallet for placing the valve body, stopper prevents pallet from moving,
    # lever pushes the pallet down
    # Profile of the valve body is checked.
    # The four sides of the valve body are scanned to check whether
    # it is matching with the profile of the predefined body or not

    # Bottom cylinder will be clamped
    time.sleep(1)
    bottom_Cylinder = 1
    s.Bottom_Cylinder.set_value(bottom_Cylinder)
    print('Bottom cylinder: Pallet clamped \n')
    clamping_Cylinder =1
    s.Clamping_Cylinder.set_value(clamping_Cylinder)
    print('Clamping cylinder: Pulled out \n')
    time.sleep(2)

    # RFID tag will be read by RFID tag reader
    rFID_tag =1
    s.RFID_tag.set_value(rFID_tag)
    rFID_reader = 1
    s.RFID_reader.set_value(rFID_reader)
    print ('RFID reader reads RFID tag \n')
    time.sleep(2)
    operation()

if __name__ == '__main__':
    main()

    
