import asyncio
import time

async def print_my_s ( sleep_time , s ):
    await asyncio.sleep ( sleep_time )
    print ( s )

async def hello_async ():
    task1 = asyncio.create_task ( print_my_s ( 2 , "Hello" ) )
    task2 = asyncio.create_task ( print_my_s ( 2 , "world" ) )

    print (time.strftime('%X'))
    await task1
    print (time.strftime('%X'))
    await task2
    print (time.strftime('%X'))

asyncio.run ( hello_async () )