# vJoyTCPFeeder
Receive Joystick events in real time from a remote host via TCP and feed them to a vJoy device.

It's intended to be used along with `jstest --event`. Run `jstest --event /dev/input/js0 | nc <IP-address-of-the-host-running-this-script> 1234` on the PC where the joystick is physically plugged in.
