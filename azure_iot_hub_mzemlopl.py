from azure.iot.device import IoTHubDeviceClient

def send_2_azure_f ( **s ):
    azure_connection_string = "HostName=mmradariothub.azure-devices.net;DeviceId=iwr6843;SharedAccessKey=k8yx5ft6yrSJ8Xsti3FViAuXWxDRtBMPbI5Hvr1DfI0="
    azure_client = IoTHubDeviceClient.create_from_connection_string ( azure_connection_string )
    azure_client.connect ()
    try :
        azure_client.send_message ( f'{s}' )
    except :
        print ( "Azure error connecting or sending message")
    azure_client.shutdown()