from time import sleep
import snap7
from snap7.util import *
import struct

client = snap7.client.Client()
client.set_connection_type(0xFD)
a = client.connect('192.168.1.10', 0, 1)

print(client.get_connected())
#print(client.get_cpu_info())
area = 0x82    # area for Q memory
start = 0      # location we are going to start the read
length = 0x02     # length in bytes of the read
bit = 0        # which bit in the Q memory byte we are reading

area = snap7.snap7types.areas.PA
dbnumber = 0
amount = 1
start = 0
b = client.read_area(area, dbnumber, start, amount)
print(b)

#byte = client.read_area(area,0,start,length)
#print("Result", byte)
#print "Q0.0:",get_bool(mibyte,0,bit)
client.disconnect()
