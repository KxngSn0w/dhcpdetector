#!/usr/bin/env python
# sudo pip install scapy_http
# Make sure a packet capture software is installed


import RPi.GPIO as GPIO
import time
import scapy.all as scapy
from scapy import DHCP, ARP, BOOTP, Ether, UDP, IP

def sniff(interface):
	# iface  - choose interface
	# store  - decide whether or not to store packets in memory
	# prn    - specify call-back function
	# filter - allows us to filter packets using the Berkley Packet Filter (BPF) syntax
	scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="arp or (udp and (port 67 or 68))")   


def process_sniffed_packet(packet):
    if DHCP in packet and packet[DHCP].options[0][1] == 3:
        MAC = packet[Ether].src
        print("DHCPREQUEST detected from %s") % MAC
        # print(packet.show())
        mac_Check(MAC)


def mac_check(MAC):
    if MAC in safe_mac:
        print("MAC address %s is safe.") % MAC
    else:
        print("MAC address %s is unknown. Initiating defense systems.") % MAC
        LED(MAC)

	
def LED(MAC):
        print("Turning on LED")
        # Initiates LED output
        GPIO.output(17, True)

# Sets Common GPIO Mode
GPIO.setmode(GPIO.BCM)

# Sets Pin 17 For Output
GPIO.setup(17, GPIO.OUT)

safe_mac = ("70:85:c2:54:98:4f", "40:4e:36:83:f9:c5", "90:32:4b:65:9e:51", "50:dc:e7:be:99:7d", "98:29:a6:d0:b3:a3", "20:ab:37:74:57:54")


sniff("etho0")

