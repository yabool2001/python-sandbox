# Sprawdzić jak zastąpić funkcję datetime.timedelta, która chyba znikła

from multiprocessing  import Process, current_process
import os
from datetime import datetime
import azure_iot_hub_mzemlopl as aih
#import azure_iot_hub_kielbex as aih

def my_main ():
    my_dict = { 'id' : datetime.utcnow().strftime("%Y%m%d%H%M%S") , 'p' : 3 , 't' : 4 }
    send_2_azure_p = Process ( target = aih.send_2_azure_f , name = 'send_2_azure_p' , kwargs = my_dict )
    send_2_azure_p.start ()
    #send_2_azure_p.join ()

if __name__ == '__main__':
    my_main ()