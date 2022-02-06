from multiprocessing import Process
from datetime import datetime
import time

p_list = []

def f ( t ):
    print ( t )
    time.wait (1)

def p ():
    p = Process ( target = f , name = '' , args = ( datetime.utcnow().isoformat() , ) )

if __name__ == '__main__':
    p ()