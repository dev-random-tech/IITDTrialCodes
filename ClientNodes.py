from opcua import Client
import time
url = "opc.tcp://localhost:61032"
client = Client(url)

try:
    client.connect()
    
    Power = client.get_node("ns=2;s=Power")
    Entry_Sensor  = client.get_node("ns=2;s=Entry_Sensor")
    Order_Status  = client.get_node("ns=2;s=Order_Status" )
    Stopper = client.get_node("ns=2;s=Stopper")
    Pallet = client.get_node("ns=2;s=Pallet")
    Conveyor = client.get_node("ns=2;s=Conveyor" )
    Operational_Sensor = client.get_node("ns=2;s=Operational_Sensor" )
    Intermediate_Sensor = client.get_node("ns=2;s=Intermediate_Sensor")
    Pneumatic = client.get_node("ns=2;s=Pneumatic" )
    Lever = client.get_node("ns=2;s=Lever" )
    Profile_Status = client.get_node("ns=2;s=Profile_Status")
    Face1 = client.get_node("ns=2;s=Face1" )
    Face2 = client.get_node("ns=2;s=Face2")
    Face3 = client.get_node("ns=2;s=Face3" )
    Face4 = client.get_node("ns=2;s=Face4" )
    Bottom_Cylinder = client.get_node("ns=2;s=Bottom_Cylinder" )
    Clamping_Cylinder = client.get_node("ns=2;s=Clamping_Cylinder" )
    RFID_tag = client.get_node("ns=2;s=RFID_tag" )
    RFID_reader = client.get_node("ns=2;s=RFID_reader" )
    Gripper = client.get_node("ns=2;s=Gripper")
    Vision_Sensor = client.get_node("ns=2;s=Vision_Sensor" )
    Motor = client.get_node("ns=2;s=Motor")
    Rotation = client.get_node("ns=2;s=Rotation")
    Exit_Sensor = client.get_node("ns=2;s=Exit_Sensor" )
    Rejection = client.get_node("ns=2;s=Rejection" )
    # tags
    smps1 = client.get_node("ns=2;s=smps1")
    smps2 = client.get_node("ns=2;s=smps2")
    smps3 = client.get_node("ns=2;s=smps3")
    plc_power =  client.get_node("ns=2;s=plc_power") 
    vfd_ConnectionStatus =  client.get_node("ns=2;s=vfd_ConnectionStatus") 
    vfd_RunMode =  client.get_node("ns=2;s=vfd_RunMode") 
    vfd_ConnectionFaulted =  client.get_node("ns=2;s=vfd_ConnectionFaulted") 
    vfd_Status =  client.get_node("ns=2;s=vfd_Status") 
    vfd_TorqueDisabled =  client.get_node("ns=2;s=vfd_TorqueDisabled") 
    vfd_SafetyFault =  client.get_node("ns=2;s=vfd_SafetyFault") 
    vfd_ResetRequired =  client.get_node("ns=2;s=vfd_ResetRequired") 
    vfd_Command =  client.get_node("ns=2;s=vfd_Command") 
    vfd_SafeTorqueOff =  client.get_node("ns=2;s=vfd_SafeTorqueOff") 
    vfd_Reset =  client.get_node("ns=2;s=vfd_Reset") 
    vfd_Power =  client.get_node("ns=2;s=vfd_Power") 
    conveyorAxis =  client.get_node("ns=2;s=conveyorAxis") 
    ent_IO_Communication = client.get_node("ns=2;s=ent_IO_Communication")
    ent_IO_DataValidity = client.get_node("ns=2;s=ent_IO_DataValidity")
    
    ent_diag1_IO1 = client.get_node("ns=2;s=ent_diag1_IO1")
    ent_diag1_IO2 = client.get_node("ns=2;s=ent_diag1_IO2")
    ent_diag1_IO3 = client.get_node("ns=2;s=ent_diag1_IO3")
    ent_diag1_IO4 = client.get_node("ns=2;s=ent_diag1_IO4")
    ent_diag1_IO5 = client.get_node("ns=2;s=ent_diag1_IO5")
    ent_diag1_IO6 = client.get_node("ns=2;s=ent_diag1_IO6")
    ent_diag1_IO7 = client.get_node("ns=2;s=ent_diag1_IO7")
    ent_diag2_IO1 = client.get_node("ns=2;s=ent_diag2_IO1")
    ent_diag2_IO2 = client.get_node("ns=2;s=ent_diag2_IO2")
    ent_diag2_IO3 = client.get_node("ns=2;s=ent_diag2_IO3")
    ent_PowerSupply = client.get_node("ns=2;s=ent_PowerSupply")
    ent_DigitalOutput = client.get_node("ns=2;s=ent_DigitalOutput")
    ent_IO_DeviceError = client.get_node("ns=2;s=ent_IO_DeviceError")
    ent_IO_DeviceWarning = client.get_node("ns=2;s=ent_IO_DeviceWarning")
    ent_IO_DeviceNotification = client.get_node("ns=2;s=ent_IO_DeviceNotification")
    int_IO_Communication = client.get_node("ns=2;s=int_IO_Communication")
    int_IO_DataValidity = client.get_node("ns=2;s=int_IO_DataValidity")
    int_diag1_IO1 = client.get_node("ns=2;s=int_diag1_IO1")
    int_diag1_IO2 = client.get_node("ns=2;s=int_diag1_IO2")
    int_diag1_IO3 = client.get_node("ns=2;s=int_diag1_IO3")
    int_diag1_IO4 = client.get_node("ns=2;s=int_diag1_IO4")
    int_diag1_IO5 = client.get_node("ns=2;s=int_diag1_IO5")
    int_diag1_IO6 = client.get_node("ns=2;s=int_diag1_IO6")
    int_diag1_IO7 = client.get_node("ns=2;s=int_diag1_IO7")
    int_diag2_IO1 = client.get_node("ns=2;s=int_diag2_IO1")
    int_diag2_IO2 = client.get_node("ns=2;s=int_diag2_IO2")
    int_diag2_IO3 = client.get_node("ns=2;s=int_diag2_IO3")
    int_PowerSupply = client.get_node("ns=2;s=int_PowerSupply")
    int_DigitalOutput = client.get_node("ns=2;s=int_DigitalOutput")
    int_IO_DeviceError = client.get_node("ns=2;s=int_IO_DeviceError")
    int_IO_DeviceWarning = client.get_node("ns=2;s=int_IO_DeviceWarning")
    int_IO_DeviceNotification = client.get_node("ns=2;s=int_IO_DeviceNotification")
    redLight = client.get_node("ns=2;s=redLight")
    yellowLight = client.get_node("ns=2;s=yellowLight")
    greenLight = client.get_node("ns=2;s=greenLight")
    buzzer = client.get_node("ns=2;s=buzzer")
    auto = client.get_node("ns=2;s=auto")
    manual = client.get_node("ns=2;s=manual")
    executeOrder = client.get_node("ns=2;s=executeOrder")
    Client_disconnect = client.get_node("ns=2;s=Client_disconnect")
    

    tagListInt = [smps1,\
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
    ent_IO_Communication,\
    ent_IO_DataValidity,\
    ent_diag1_IO1,\
    ent_diag1_IO2,\
    ent_diag1_IO3,\
    ent_diag1_IO4,\
    ent_diag1_IO4,\
    ent_diag1_IO4,\
    ent_diag1_IO1,\
    ent_diag2_IO2,\
    ent_diag2_IO3,\
    ent_PowerSupply,\
    ent_IO_DeviceError,\
    ent_IO_DeviceWarning,\
    ent_IO_DeviceNotification,\
    int_DigitalOutput,\
    int_IO_Communication,\
    int_IO_DataValidity,\
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
    
    tagList = list(map(bool,tagListInt))

except:
    print('')