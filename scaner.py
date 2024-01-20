    #!/usr/bin/env/ python
    #_*_ coding: utf8 _*_

    from scapy.all import *
    parse = argparse.ArgumentParser()
    parse.add_argument("-r","--rango",help="Rango de direcciones a escanear")
    parse = parse.parse_args()
     
    def ip_scan(ip):
        try:
            range_ip = ARP(pdst=ip+"/24") #pdst rango de ips
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff") #Ether se trabaja en capa 3, dst direccion mac default
            final_packet = broadcast/range_ip
            res = srp(final_packet, timeout=2, verbose=False)[0] #para quedar a la escucha, [0] accede a posicion 0 d ela tupla
            for n in res:
                print("[+]Host: {} -- MAC: {}".format(n[1].psrc, n[1].hwsrc)) #pcrs direccion ip
        except Exception as ex:
            print("Error: {}".format(ex))
     
    def main():
        if parse.rango:
            ip_scan(parse.rango)
        else:
            print("Necesito un rango de ips al escanear")
        
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print("Saliendo")
            exit()