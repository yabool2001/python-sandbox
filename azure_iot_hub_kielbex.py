from azure.iot.device import IoTHubDeviceClient

def send_2_azure_f ( **s ):
    azure_connection_string = "HostName=mmradarIH.azure-devices.net;DeviceId=iwr6843isk;SharedAccessKey=WFV3cmknUqGc1S5OZJSMcgF4Uub1n9tho/fAK8CTWYE="
    azure_client = IoTHubDeviceClient.create_from_connection_string ( azure_connection_string )
    azure_client.connect ()
    try :
        azure_client.send_message ( f'{s}' )
    except :
        print ( "Azure error connecting or sending message")
    azure_client.shutdown()