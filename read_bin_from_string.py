import struct

data = b'\x01\x00\x00\x00\x02\x00\x00\x00'

x , y = struct.unpack ( '2I' , data )
print ( x , y )

file = open ( 'string_with_bin.txt' , 'r' )
line = file.readline ()
data_line = bytes (line,'ascii')
print ( data_line )
#x , y = struct.unpack ( '2I' , file_data )
#print ( x , y )
