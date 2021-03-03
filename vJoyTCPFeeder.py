#!/usr/bin/env python3 

import socket
import pyvjoy
import parse

# from joystick.h
JS_EVENT_BUTTON = 0x01
JS_EVENT_AXIS = 0x02
JS_EVENT_INIT = 0x80

eventFormat = "Event: type {type:d}, time {time:d}, " + \
    "number {number:d}, value {value:d}\n"

def parseEventAndFeed(l, j1, j2):
    r = parse.parse(eventFormat, l)
    if r:
        #print(r.named)
        type = r.named['type']
        number = r.named['number']
        value = r.named['value']
        if (type & JS_EVENT_BUTTON != 0):
            j1.set_button(number+1, value)
        if (type & JS_EVENT_AXIS != 0):
            if number < 8:
                j1.set_axis(number+pyvjoy.HID_USAGE_LOW, (value + 32769)//2)
            else:
                j2.set_axis(number-8+pyvjoy.HID_USAGE_LOW, (value + 32769)//2)


if __name__ == "__main__": 
    j1 = pyvjoy.VJoyDevice(1)
    j2 = pyvjoy.VJoyDevice(2)
    with socket.create_server(('', 1234), family=socket.AF_INET) as s:
        conn, addr = s.accept()
        with conn:
            print('Connected by:', addr)
            with conn.makefile(buffering=1) as f:
                while True:
                    l = f.readline()
                    if not l:
                        break
                    else:
                        parseEventAndFeed(l, j1, j2)
                        #print(l)
    pass