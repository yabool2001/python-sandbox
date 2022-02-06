import asyncio
import time

sleep_time = 2

async def my_loop ( s ):
    for i in range ( 1 , 2 ):
        print ( time.strftime('%X') )
        await asyncio.sleep ( sleep_time ) # always suspends the current task, allowing other tasks to run.
        print ( f"{s}:  {i}" )
        print ( time.strftime('%X') )

async def gather ():
    my_list = await asyncio.gather ( my_loop ( "Task 1") , my_loop ( "Task 2") )

asyncio.run ( gather () )
