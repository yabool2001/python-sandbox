import struct
import gzip

data = b'\x01\x00\x00\x00\x02\x00\x00\x00'
data_x , data_y = struct.unpack ( '2I' , data )
print ( data_x , data_y )

s = open ( 'string_with_bin.txt' , 'r' ) .readline ()
b = eval ( s )
b_x , b_y = struct.unpack ( '2I' , b )
print ( b_x , b_y )
