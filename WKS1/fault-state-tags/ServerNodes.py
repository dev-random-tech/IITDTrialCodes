from opcua import Server
import time

server = Server()
url = "opc.tcp://localhost:61032"
server.set_endpoint(url)
node = server.get_objects_node()

Power = node.add_variable("ns=2;s=Power" , "power" , 0)
Entry_Sensor  = node.add_variable("ns=2;s=Entry_Sensor" , "entry_Sensor" , 0)
Order_Status  = node.add_variable("ns=2;s=Order_Status" , "order_Status" , False)
Pallet  = node.add_variable("ns=2;s=Pallet" , "pallet" , '')
Stopper = node.add_variable("ns=2;s=Stopper" , "stopper" , 0)
Conveyor = node.add_variable("ns=2;s=Conveyor" , "conveyor" , 0)
Operational_Sensor = node.add_variable("ns=2;s=Operational_Sensor" , "operational_Sensor" , 0)
Intermediate_Sensor = node.add_variable("ns=2;s=Intermediate_Sensor" , "intermediate_Sensor" , 0)
Pneumatic = node.add_variable("ns=2;s=Pneumatic" , "pneumatic" , 0)
Lever = node.add_variable("ns=2;s=Lever" , "lever" , 0)
Profile_Status = node.add_variable("ns=2;s=Profile_Status" , "profile_Status" , '0')
Face1 = node.add_variable("ns=2;s=Face1" , "face1" , 0)
Face2 = node.add_variable("ns=2;s=Face2" , "face2" , 0)
Face3 = node.add_variable("ns=2;s=Face3" , "face3" , 0)
Face4 = node.add_variable("ns=2;s=Face4" , "face4" , 0)
Bottom_Cylinder = node.add_variable("ns=2;s=Bottom_Cylinder" , "bottom_Cylinder" , 0)
Clamping_Cylinder = node.add_variable("ns=2;s=Clamping_Cylinder" , "clamping_Cylinder" , 0)
RFID_tag = node.add_variable("ns=2;s=RFID_tag" , "rFID_tag" , 0)
RFID_reader = node.add_variable("ns=2;s=RFID_reader" , "rFID_reader" , 0)
Gripper = node.add_variable("ns=2;s=Gripper" , "gripper" , 0)
Vision_Sensor = node.add_variable("ns=2;s=Vision_Sensor" , "vision_Sensor" , 0)
Motor = node.add_variable("ns=2;s=Motor" , "motor" , 0)
Rotation = node.add_variable("ns=2;s=Rotation" , "rotation" , 0)
Exit_Sensor = node.add_variable("ns=2;s=Exit_Sensor" , "exit_Sensor" , 0)
Rejection = node.add_variable("ns=2;s=Rejection" , "rejection" , 0)
# tags
smps1 = node.add_variable("ns=2;s=smps1", "SMPS1", 1)
smps2 = node.add_variable("ns=2;s=smps2", "SMPS2", 1)
smps3 = node.add_variable("ns=2;s=smps3", "SMPS3", 1)
plc_power =  node.add_variable("ns=2;s=plc_power", "Plc_power", 1) 
vfd_ConnectionStatus =  node.add_variable("ns=2;s=vfd_ConnectionStatus", "Vfd_ConnectionStatus", 1) 
vfd_RunMode =  node.add_variable("ns=2;s=vfd_RunMode", "Vfd_RunMode", 1) 
vfd_ConnectionFaulted =  node.add_variable("ns=2;s=vfd_ConnectionFaulted", "Vfd_ConnectionFaulted", 0) 
vfd_Status =  node.add_variable("ns=2;s=vfd_Status", "Vfd_Status", 0) 
vfd_TorqueDisabled =  node.add_variable("ns=2;s=vfd_TorqueDisabled", "Vfd_TorqueDisabled", 0) 
vfd_SafetyFault =  node.add_variable("ns=2;s=vfd_SafetyFault", "Vfd_SafetyFault", 0) 
vfd_ResetRequired =  node.add_variable("ns=2;s=vfd_ResetRequired", "Vfd_ResetRequired", 0) 
vfd_Command =  node.add_variable("ns=2;s=vfd_Command", "Vfd_Command", 0) 
vfd_SafeTorqueOff =  node.add_variable("ns=2;s=vfd_SafeTorqueOff", "Vfd_SafeTorqueOff", 0) 
vfd_Reset =  node.add_variable("ns=2;s=vfd_Reset", "Vfd_Reset", 0) 
vfd_Power =  node.add_variable("ns=2;s=vfd_Power", "Vfd_Power", 1) 
conveyorAxis =  node.add_variable("ns=2;s=conveyorAxis", "ConveyorAxis", 1) 
# Entry Sensor tags
ent_IO_Communication = node.add_variable("ns=2;s=ent_IO_Communication", "Ent_IO_Communication", 1)
ent_IO_DataValidity = node.add_variable("ns=2;s=ent_IO_DataValidity", "Ent_IO_DataValidity", 0)
ent_diag1_IO1 = node.add_variable("ns=2;s=ent_diag1_IO1", "Ent_diag1_IO1", 0)
ent_diag1_IO2 = node.add_variable("ns=2;s=ent_diag1_IO2", "Ent_diag1_IO2", 0)
ent_diag1_IO3 = node.add_variable("ns=2;s=ent_diag1_IO3", "Ent_diag1_IO3", 0)
ent_diag1_IO4 = node.add_variable("ns=2;s=ent_diag1_IO4", "Ent_diag1_IO4", 0)
ent_diag1_IO5 = node.add_variable("ns=2;s=ent_diag1_IO5", "Ent_diag1_IO5", 0)
ent_diag1_IO6 = node.add_variable("ns=2;s=ent_diag1_IO6", "Ent_diag1_IO6", 0)
ent_diag1_IO7 = node.add_variable("ns=2;s=ent_diag1_IO7", "Ent_diag1_IO7", 0)
ent_diag2_IO1 = node.add_variable("ns=2;s=ent_diag2_IO1", "Ent_diag2_IO1", 0)
ent_diag2_IO2 = node.add_variable("ns=2;s=ent_diag2_IO2", "Ent_diag2_IO2", 0)
ent_diag2_IO3 = node.add_variable("ns=2;s=ent_diag2_IO3", "Ent_diag2_IO3", 0)
ent_PowerSupply = node.add_variable("ns=2;s=ent_PowerSupply", "Ent_PowerSupply", 1)
ent_DigitalOutput = node.add_variable("ns=2;s=ent_DigitalOutput", "Ent_DigitalOutput", 1)
ent_IO_DeviceError = node.add_variable("ns=2;s=ent_IO_DeviceError", "Ent_IO_DeviceError", 0)
ent_IO_DeviceWarning = node.add_variable("ns=2;s=ent_IO_DeviceWarning", "Ent_IO_DeviceWarning", 0)
ent_IO_DeviceNotification = node.add_variable("ns=2;s=ent_IO_DeviceNotification", "Ent_IO_DeviceNotification", 0)
# Intermediate Sensor Tags
int_IO_Communication = node.add_variable("ns=2;s=int_IO_Communication", "Int_IO_Communication", 1)
int_IO_DataValidity = node.add_variable("ns=2;s=int_IO_DataValidity", "Int_IO_DataValidity", 0)
int_diag1_IO1 = node.add_variable("ns=2;s=int_diag1_IO1", "Int_diag1_IO1", 0)
int_diag1_IO2 = node.add_variable("ns=2;s=int_diag1_IO2", "Int_diag1_IO2", 0)
int_diag1_IO3 = node.add_variable("ns=2;s=int_diag1_IO3", "Int_diag1_IO3", 0)
int_diag1_IO4 = node.add_variable("ns=2;s=int_diag1_IO4", "Int_diag1_IO4", 0)
int_diag1_IO5 = node.add_variable("ns=2;s=int_diag1_IO5", "Int_diag1_IO5", 0)
int_diag1_IO6 = node.add_variable("ns=2;s=int_diag1_IO6", "Int_diag1_IO6", 0)
int_diag1_IO7 = node.add_variable("ns=2;s=int_diag1_IO7", "Int_diag1_IO7", 0)
int_diag2_IO1 = node.add_variable("ns=2;s=int_diag2_IO1", "Int_diag2_IO1", 0)
int_diag2_IO2 = node.add_variable("ns=2;s=int_diag2_IO2", "Int_diag2_IO2", 0)
int_diag2_IO3 = node.add_variable("ns=2;s=int_diag2_IO3", "Int_diag2_IO3", 0)
int_PowerSupply = node.add_variable("ns=2;s=int_PowerSupply", "Int_PowerSupply", 1)
int_DigitalOutput = node.add_variable("ns=2;s=int_DigitalOutput", "Int_DigitalOutput", 1)
int_IO_DeviceError = node.add_variable("ns=2;s=int_IO_DeviceError", "Int_IO_DeviceError", 0)
int_IO_DeviceWarning = node.add_variable("ns=2;s=int_IO_DeviceWarning", "Int_IO_DeviceWarning", 0)
int_IO_DeviceNotification = node.add_variable("ns=2;s=int_IO_DeviceNotification", "Int_IO_DeviceNotification", 0)
# Tower Light Tag
redLight = node.add_variable("ns=2;s=redLight", "RedLight", 0)
yellowLight = node.add_variable("ns=2;s=yellowLight", "YellowLight", 0)
greenLight = node.add_variable("ns=2;s=greenLight", "GreenLight", 0)
buzzer = node.add_variable("ns=2;s=buzzer", "Buzzer", 0)
# Station Mode Tag
auto = node.add_variable("ns=2;s=auto", "Auto", 1)
manual = node.add_variable("ns=2;s=manual", "Manual", 0)
# Order Tag
executeOrder = node.add_variable("ns=2;s=executeOrder", "ExecuteOrder", 1)

Client_disconnect = node.add_variable("ns=2;s=Client_disconnect", "client_disconnect", 0)


Power.set_writable()
Entry_Sensor.set_writable()
Order_Status.set_writable()
Stopper.set_writable()
Conveyor.set_writable()
Pallet.set_writable()
Rotation.set_writable()
Operational_Sensor.set_writable()
Intermediate_Sensor.set_writable()
Pneumatic.set_writable()
Lever.set_writable()
Profile_Status.set_writable()
Face1.set_writable()
Face2.set_writable()
Face3.set_writable()
Face4.set_writable()
Bottom_Cylinder.set_writable()
Clamping_Cylinder.set_writable()
RFID_tag.set_writable()
RFID_reader.set_writable()
Gripper.set_writable()
Vision_Sensor.set_writable()
Motor.set_writable()
Exit_Sensor.set_writable()
Rejection.set_writable()
Client_disconnect.set_writable()

#tags
smps1.set_writable()
smps2.set_writable()
smps3.set_writable()
plc_power.set_writable()
vfd_ConnectionStatus.set_writable()
vfd_RunMode.set_writable()
vfd_ConnectionFaulted.set_writable()
vfd_Status.set_writable()
vfd_TorqueDisabled.set_writable()
vfd_SafetyFault.set_writable()
vfd_ResetRequired.set_writable()
vfd_Command.set_writable()
vfd_SafeTorqueOff.set_writable()
vfd_Reset.set_writable()
vfd_Power.set_writable()
conveyorAxis.set_writable()
ent_IO_Communication.set_writable()
ent_IO_DataValidity.set_writable()
ent_diag1_IO1.set_writable()
ent_diag1_IO2.set_writable()
ent_diag1_IO3.set_writable()
ent_diag1_IO4.set_writable()
ent_diag1_IO5.set_writable()
ent_diag1_IO6.set_writable()
ent_diag1_IO7.set_writable()
ent_diag2_IO1.set_writable()
ent_diag2_IO2.set_writable()
ent_diag2_IO3.set_writable()
ent_PowerSupply.set_writable()
ent_DigitalOutput.set_writable()
ent_IO_DeviceError.set_writable()
ent_IO_DeviceWarning.set_writable()
ent_IO_DeviceNotification.set_writable()
int_IO_Communication.set_writable()
int_IO_DataValidity.set_writable()
int_diag1_IO1.set_writable()
int_diag1_IO2.set_writable()
int_diag1_IO3.set_writable()
int_diag1_IO4.set_writable()
int_diag1_IO5.set_writable()
int_diag1_IO6.set_writable()
int_diag1_IO7.set_writable()
int_diag2_IO1.set_writable()
int_diag2_IO2.set_writable()
int_diag2_IO3.set_writable()
int_PowerSupply.set_writable()
int_DigitalOutput.set_writable()
int_IO_DeviceError.set_writable()
int_IO_DeviceWarning.set_writable()
int_IO_DeviceNotification.set_writable()
redLight.set_writable()
yellowLight.set_writable()
greenLight.set_writable()
buzzer.set_writable()
auto.set_writable()
manual.set_writable()
executeOrder.set_writable()

server.start()
print("Server started \n")
