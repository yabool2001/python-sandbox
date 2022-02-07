# Sprawdzić jak zastąpić funkcję datetime.timedelta, która chyba znikła

from multiprocessing  import Process, current_process
import os
import azure_iot_hub_mzemlopl as aih
#import azure_iot_hub_kielbex as aih

def my_main ():
    send_2_azure_p = Process ( target = aih.send_2_azure , name = 'send_2_azure_p' )
    send_2_azure_p.start ()
    #send_2_azure_p.join ()

if __name__ == '__main__':
    my_main ()
