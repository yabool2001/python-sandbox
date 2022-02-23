from azure.iot.device import IoTHubDeviceClient
from datetime import datetime, timedelta
from multiprocessing import Process
import random
import time

simulation_duration = 60
message_period = 3

pl = []

def send_2_azure ():
    
    try :
        #azure_client.send_message ( f'{my_dict}' )
        print ( f'{my_dict}' )
    except :
        print ( "Azure error sending message" )

if __name__ == '__main__':
    azure_connection_string = "HostName=mmradariothub.azure-devices.net;DeviceId=iwr6843;SharedAccessKey=k8yx5ft6yrSJ8Xsti3FViAuXWxDRtBMPbI5Hvr1DfI0="
    azure_client = IoTHubDeviceClient.create_from_connection_string ( azure_connection_string )
    azure_client.connect ()

    simulation_time_up = datetime.utcnow () + timedelta ( seconds = simulation_duration )
    while datetime.utcnow () < simulation_time_up :
        my_dict = { 'id' : datetime.utcnow().strftime("%Y%m%d%H%M%S") , 'p' : {random.randint ( 0 , 10 )} , 't' : {random.randint ( 0 , 10 )} }
        p = Process ( target = send_2_azure () , args = ( my_dict , ) , name = my_dict['id'] )
        pl.append ( p )
        p.start ()

        time.sleep ( message_period )

    azure_client.shutdown ()
