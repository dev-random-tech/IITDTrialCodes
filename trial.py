import datetime
import time
import sys
import ttg
import numpy as np
import pandas
from opcua import Client


# input_table = ttg.Truths(['A_1','A_2','A_3','B_1','B_2','B_3'])
# input_dataframe = input_table.as_pandas()

# Fault of the machine at which component or why || 


 
    smps1 = bool(randint(0,1))
    smps2 = randint(0,1)
    smps3 = randint(0,1)
    plc_power = randint(0,1)
    vfd_ConnectionStatus = randint(0,1)
    vfd_RunMode = randint(0,1)
    vfd_ConnectionFaulted = randint(0,1)
    vfd_Status = randint(0,1)
    vfd_TorqueDisabled = randint(0,1)
    vfd_SafetyFault = randint(0,1)
    vfd_ResetRequired = randint(0,1)
    vfd_Command = randint(0,1)
    vfd_SafeTorqueOff = randint(0,1)
    vfd_Reset = randint(0,1)
    vfd_Power = randint(0,1)
    conveyorAxis = randint(0,1)
    ent_DigitalOutput = randint(0,1)
    ent_DataModeIO = randint(0,1)
    ent_DataValidity = randint(0,1)
    ent_diag1_IO1 = randint(0,1)
    ent_diag1_IO2 = randint(0,1)
    ent_diag1_IO3 = randint(0,1)
    ent_diag1_IO4 = randint(0,1)
    ent_diag1_IO5 = randint(0,1)
    ent_diag1_IO6 = randint(0,1)
    ent_diag1_IO1 = randint(0,1)
    ent_diag2_IO2 = randint(0,1)
    ent_diag2_IO3 = randint(0,1)
    ent_PowerSupply = randint(0,1)
    ent_IO_DeviceError = randint(0,1)
    ent_IO_DeviceWarning = randint(0,1)
    ent_IO_DeviceNotification = randint(0,1)
    int_DigitalOutput = randint(0,1)
    int_DataModeIO = randint(0,1)
    int_DataValid = randint(0,1)
    int_diag1_IO1 = randint(0,1)
    int_diag1_IO2 = randint(0,1)
    int_diag1_IO3 = randint(0,1)
    int_diag1_IO4 = randint(0,1)
    int_diag1_IO5 = randint(0,1)
    int_diag1_IO6 = randint(0,1)
    int_diag2_IO1 = randint(0,1)
    int_diag2_IO2 = randint(0,1)
    int_diag2_IO3 = randint(0,1)
    int_PowerSupply = randint(0,1)
    int_IO_DeviceError = randint(0,1)
    int_IO_DeviceWarning = randint(0,1)
    int_IO_DeviceNotification = randint(0,1)
    redLight = randint(0,1)
    yellowLight = randint(0,1)
    greenLight = randint(0,1)
    buzzer = randint(0,1)
    auto = randint(0,1)
    manual = randint(0,1)
    executeOrder = randint(0,1)

tagList = list(map(bool,tagListInt))

powerSystem = smps1 and smps2 and smps3

fault_reasons = [not smps1,\
not smps2,\
not smps3,\
not plc_power,\
not vfd_Power and (not vfd_ConnectionStatus),\
not vfd_Power and (not vfd_SafetyFault),\
not vfd_Power,\
not ent_DataModeIO,\
powerSystem and ent_diag1_IO1,\
powerSystem and ent_diag1_IO2,\
powerSystem and ent_diag1_IO3,\
powerSystem and ent_diag1_IO4,\
powerSystem and ent_diag1_IO5,\
powerSystem and ent_diag1_IO6,\
powerSystem and ent_PowerSupply,\
powerSystem and ent_IO_DeviceError,\
powerSystem and ent_IO_DeviceWarning,\
powerSystem and not int_DataModeIO,\
powerSystem and int_diag1_IO1,\
powerSystem and int_diag1_IO2,\
powerSystem and int_diag1_IO3,\
powerSystem and int_diag1_IO4,\
powerSystem and int_diag1_IO5,\
powerSystem and int_diag1_IO5,\
powerSystem and int_PowerSupply,\
powerSystem and int_IO_DeviceError,\
powerSystem and int_IO_DeviceWarning]

status = np.array([])

faults = np.array(['SMPS-1',\
'SMPS-2',\
'SMPS-3',\

'Power to PLC',\

'VFD Connections',\
'VFD Safety Requirements',\
'VFD Power Connection',\

'Entry Sensor: not in IO Link Connection Mode',\
'Entry Sensor: Low Voltage at Sensor Power Supply',\
'Entry Sensor: Low Voltage at AUX Power Supply'\
'Entry Sensor: Short Circuit',\
'Entry Sensor: Short Circuit at Actuator Channel A',\
'Entry Sensor: Short Circuit at Actuator Channel B',\
'Entry Sensor: IO Link not verified',\
'Entry Sensor: Connected to wrong device or No device found connected to IO Link'\
'Entry Sensor: IO Link Device Warning',\
'Entry Sensor: Power Supply Issues',\
'Entry Sensor: Device Error',\
'Entry Sensor: Device Warning',\

'Intermediate Sensor: not in IO Link Connection Mode',\
'Intermediate Sensor: Low Voltage at Sensor Power Supply',\
'Intermediate Sensor: Low Voltage at AUX Power Supply'\
'Intermediate Sensor: Short Circuit',\
'Intermediate Sensor: Short Circuit at Actuator Channel A',\
'Intermediate Sensor: Short Circuit at Actuator Channel B',\
'Intermediate Sensor: IO Link not verified',\
'Intermediate Sensor: Connected to wrong device or No device found connected to IO Link'\
'Intermediate Sensor: IO Link Device Warning',\
'Intermediate Sensor: Power Supply Issues',\
'Intermediate Sensor: Device Error',\
'Intermediate Sensor: Device Warning'])

print('Faults at: ',faults[fault_reasons])


'''
Values after the tags are values indicating correct functioning of machine

vfd:SI.ConnectionStatus opposite to vfd:Sl.ConnectionFaulted | 1
vfd:SI.RunMode | 1
vfd:SI.Status | 0
vfd:SI.TorqueDisable | 0
vfd:SI.ResetRequired | 0
vfd:SO.Command | 0
vfd:SO.SafeTorqueOff | 0
vfd:SO.Reset | 0

EM05_ConveyorAxis_C.ip | 1 = Running

Digital input for Entry Sensor | 1 = Object in front of it
IO Link Process Validity | 0
IO Link Device Notification | 0
Entry Sensor: Moderate Notification | 0

Red Light | 1 = Station Error
Yellow Light | 1 = Waiting for Order
Green Light | 1 = In Executing Mode
buzz | 1 = Emergency is Pressed

Mode_Auto | 1 = Running in Auto Mode
Mode_Manual | 1 = Running in Manual Mode

Command Execute Order | 

'''
