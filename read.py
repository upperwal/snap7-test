import snap7.client as c
from snap7.util import *
from snap7.snap7types import *
import time


def ReadMemory(plc, byte, bit, datatype):
    result = plc.read_area(areas["MK"], 0, byte, datatype)
    if datatype == S7WLBit:
        return get_bool(result, 0, 1)
    elif datatype == S7WLByte or datatype == S7WLWord:
        return get_int(result, 0)
    elif datatype == S7WLReal:
        return get_real(result, 0)
    elif datatype == S7WLDWord:
        return get_dword(result, 0)
    else:
        return None

if __name__ == "__main__":
    plc = c.Client()
    plc.connect('192.168.1.10', 0, 1)
    #for i in range(40):
    print ReadMemory(plc, 40, 0, S7WLReal)
    #time.sleep(0.5)
    for i in range(11):
        print(get_real(plc.db_read(1, 4 * i, S7WLReal), 0))
    for i in range(8):
        print(get_bool(plc.db_read(1, 44, S7WLDWord), 0, i))
    s = bytearray(1)
    s[0] = 0
    print(plc.write_area(areas["MK"], 0, 3, s))
