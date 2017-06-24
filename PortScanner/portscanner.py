# PREREQUISITE MODULES
from socket import * 
import sys, time 
from datetime import datetime 

# PROGRAM SETTINGS
host = ''
max_port = 10000
min_port = 1

def scan_host(host, port, r_code = 1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((host,port)) 
        if code == 0:
            r_code = code
        s.close()
    except Exception, e:
        pass
    return r_code 

# INITIATING SCAN
try:
    host = raw_input("[*] Enter the target host's address!")
except KeyboardInterrupt:
    print("\n\n [*] User requested an interrupt.")
    print("[*] Application shutting down")
    sys.exit(1)

# Return value of host IP / URL 
hostip = gethostbyname(host)
print("\n [*] HOST %s IP %s" % (host,hostip))

print("[*] Scanning started at %s... \n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

# Scanning process
for port in range(min_port, max_port):
    try:
        response = scan_host(host,port)

        if response == 0:
            print("[*] Port %d: Open" % (port))
    except Exception, e:
        pass

stop_time = datetime.now()
total_time = stop_time - start_time
print("\n [*] Scanning finished at %s ..." % (time.strftime("%H:%M:%S"))) 
print("[*] Scanning duration: %s ... " % (total_time))
print("f4l4f3lr41d3r thanks you for your time. Hope you had fun. :-) ")  


