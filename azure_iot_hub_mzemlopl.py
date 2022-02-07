from azure.iot.device import IoTHubDeviceClient
from datetime import datetime, timedelta
import time

simulation_duration = 360
message_period = 3

def send_2_azure ():
    azure_connection_string = "HostName=mmradariothub.azure-devices.net;DeviceId=iwr6843;SharedAccessKey=k8yx5ft6yrSJ8Xsti3FViAuXWxDRtBMPbI5Hvr1DfI0="
    azure_client = IoTHubDeviceClient.create_from_connection_string ( azure_connection_string )
    azure_client.connect ()
    
    simulation_time_up = datetime.utcnow () + timedelta ( seconds = simulation_duration )
    while datetime.utcnow () < simulation_time_up :
        my_dict = { 'id' : datetime.utcnow().strftime("%Y%m%d%H%M%S") , 'p' : 3 , 't' : 4 }
        try :
            azure_client.send_message ( f'{my_dict}' )
        except :
            print ( "Azure error connecting or sending message" )
        time.sleep ( message_period )
    azure_client.shutdown ()