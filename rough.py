import datetime
import time
import numpy as np
from operator import and_

# input_table = ttg.Truths(['A_1','A_2','A_3','B_1','B_2','B_3'])
# input_dataframe = input_table.as_pandas()

# Fault of the machine at which component or why || 
#Right Values
def xnor_(a,b):
    
def faults(tags):
    smps1 = True
    smps2 = True
    smps3 = True

    plc_power = True
    vfd_ConnectionStatus = True
    vfd_RunMode = True
    vfd_ConnectionFaulted = False
    vfd_Status = False
    vfd_TorqueDisabled = False
    vfd_SafetyFault = False
    vfd_ResetRequired = False
    vfd_Command = False
    vfd_SafeTorqueOff = False
    vfd_Reset = False
    vfd_Power = True
    conveyorAxis = True
    ent_DigitalOutput = True
    ent_DataModeIO = True
    ent_DataValidity = False
    ent_diag1_IO1 = False
    ent_diag1_IO2 = False
    ent_diag1_IO3 = False
    ent_diag1_IO4 = False
    ent_diag1_IO5 = False
    ent_diag1_IO6 = False
    ent_diag1_IO1 = False
    ent_diag2_IO2 = False
    ent_diag2_IO3 = False
    ent_PowerSupply = True
    ent_IO_DeviceError = False
    ent_IO_DeviceWarning = False
    ent_IO_DeviceNotification = False
    int_DigitalOutput = True
    int_DataModeIO = True
    int_DataValidity = False
    int_diag1_IO1 = False
    int_diag1_IO2 = False
    int_diag1_IO3 = False
    int_diag1_IO4 = False
    int_diag1_IO5 = False
    int_diag1_IO6 = False
    int_diag2_IO1 = False
    int_diag2_IO2 = False
    int_diag2_IO3 = False
    int_PowerSupply = True
    int_IO_DeviceError = False
    int_IO_DeviceWarning = False
    int_IO_DeviceNotification = False
    redLight = False
    yellowLight = False
    greenLight = False
    buzzer = False
    auto = True
    manual = True
    executeOrder = True

    tagsCompare = [smps1,\
    smps2,\
    smps3,\
    plc_power,\
    vfd_ConnectionStatus,\
    vfd_RunMode,\
    vfd_ConnectionFaulted,\
    vfd_Status,\
    vfd_TorqueDisabled,\
    vfd_SafetyFault,\
    vfd_ResetRequired,\
    vfd_Command,\
    vfd_SafeTorqueOff,\
    vfd_Reset,\
    vfd_Power,\
    conveyorAxis,\
    ent_DigitalOutput,\
    ent_DataModeIO,\
    ent_DataValidity,\
    ent_diag1_IO1,\
    ent_diag1_IO2,\
    ent_diag1_IO3,\
    ent_diag1_IO4,\
    ent_diag1_IO5,\
    ent_diag1_IO6,\
    ent_diag1_IO1,\
    ent_diag2_IO2,\
    ent_diag2_IO3,\
    ent_PowerSupply,\
    ent_IO_DeviceError,\
    ent_IO_DeviceWarning,\
    ent_IO_DeviceNotification,\
    int_DigitalOutput,\
    int_DataModeIO,\
    int_DataValidity,\
    int_diag1_IO1,\
    int_diag1_IO2,\
    int_diag1_IO3,\
    int_diag1_IO4,\
    int_diag1_IO5,\
    int_diag1_IO6,\
    int_diag2_IO1,\
    int_diag2_IO2,\
    int_diag2_IO3,\
    int_PowerSupply,\
    int_IO_DeviceError,\
    int_IO_DeviceWarning,\
    int_IO_DeviceNotification,\
    redLight,\
    yellowLight,\
    greenLight,\
    buzzer,\
    auto,\
    manual,\
    executeOrder]

    new_list = list(map(and_,tags,tagsCompare))
    if (any(new_list)):
        (smps1,\
        smps2,\
        smps3,\
        plc_power,\
        vfd_ConnectionStatus,\
        vfd_RunMode,\
        vfd_ConnectionFaulted,\
        vfd_Status,\
        vfd_TorqueDisabled,\
        vfd_SafetyFault,\
        vfd_ResetRequired,\
        vfd_Command,\
        vfd_SafeTorqueOff,\
        vfd_Reset,\
        vfd_Power,\
        conveyorAxis,\
        ent_DigitalOutput,\
        ent_DataModeIO,\
        ent_DataValidity,\
        ent_diag1_IO1,\
        ent_diag1_IO2,\
        ent_diag1_IO3,\
        ent_diag1_IO4,\
        ent_diag1_IO5,\
        ent_diag1_IO6,\
        ent_diag1_IO1,\
        ent_diag2_IO2,\
        ent_diag2_IO3,\
        ent_PowerSupply,\
        ent_IO_DeviceError,\
        ent_IO_DeviceWarning,\
        ent_IO_DeviceNotification,\
        int_DigitalOutput,\
        int_DataModeIO,\
        int_DataValidity,\
        int_diag1_IO1,\
        int_diag1_IO2,\
        int_diag1_IO3,\
        int_diag1_IO4,\
        int_diag1_IO5,\
        int_diag1_IO6,\
        int_diag2_IO1,\
        int_diag2_IO2,\
        int_diag2_IO3,\
        int_PowerSupply,\
        int_IO_DeviceError,\
        int_IO_DeviceWarning,\
        int_IO_DeviceNotification,\
        redLight,\
        yellowLight,\
        greenLight,\
        buzzer,\
        auto,\
        manual,\
        executeOrder) = tags

        powerSystem = smps1 and smps2 and smps3

        fault_reasons = [not smps1,\
        not smps2,\
        not smps3,\
        not plc_power,\
        not vfd_Power and (not vfd_ConnectionStatus),\
        not vfd_Power and (not vfd_SafetyFault),\
        not vfd_Power,\
        powerSystem and (not ent_DataModeIO),\
        powerSystem and ent_diag1_IO1,\
        powerSystem and ent_diag1_IO2,\
        powerSystem and ent_diag1_IO3,\
        powerSystem and ent_diag1_IO4,\
        powerSystem and ent_diag1_IO5,\
        powerSystem and ent_diag1_IO6,\
        powerSystem and (not ent_PowerSupply),\
        powerSystem and ent_IO_DeviceError,\
        powerSystem and ent_IO_DeviceWarning,\
        powerSystem and (not int_DataModeIO),\
        powerSystem and int_diag1_IO1,\
        powerSystem and int_diag1_IO2,\
        powerSystem and int_diag1_IO3,\
        powerSystem and int_diag1_IO4,\
        powerSystem and int_diag1_IO5,\
        powerSystem and int_diag1_IO5,\
        powerSystem and (not int_PowerSupply),\
        powerSystem and int_IO_DeviceError,\
        powerSystem and int_IO_DeviceWarning]


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

