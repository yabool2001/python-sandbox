from multiprocessing  import Process, current_process, Pool
import os
import time

procs_list = []

def func1 ( s ):
    time.sleep ( 5 )
    print (f'{s} {current_process ().name} {os.getpid ()}')
    print ( time.strftime('%X') )

def my_main ():
    p1 = Process ( target = func1 , args = ('p1' , ) , name = 'p1' , daemon = True )
    p1.start ()
    p1.join ()

if __name__ == '__main__':
    my_main ()
