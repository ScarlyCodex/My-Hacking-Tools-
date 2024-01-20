import nmap 

def main():
    scaner = nmap.PortScanner()
    ip = input("IP--> ")
    scaner.scan(hosts=ip, arguments='--top-ports 1000 -sV --version-intensity 3')
    

if __name__ == '__main__':
    main()
