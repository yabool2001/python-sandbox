import os
import platform
print (os.name)
print (platform.system())
if os.name == 'Windows':
    print ( '/dev/' + s_p.name )
elif os.name == 'posix':
    print ( s_p.name )