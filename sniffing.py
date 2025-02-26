#!/usr/bin/python3

from scapy.all import *

print("Sniffing Packets (Case #1: ICMP)")
print("-----------")
def print_pkt(pkt):
    pkt. show()

pkt = sniff(filter='icmp',prn=print_pkt)
#ping www.google.com
