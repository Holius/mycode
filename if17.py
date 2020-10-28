#!/usr/bin/env python3
ipchk = input("Apply an IP address: ")

# checks if IP entered is gateway
if ipchk == "192.168.70.1": print("That's our Gateway address!  Nope!")
elif ipchk: print("Looks like the IP address was set: " + ipchk)
else: print("Study Net+ to learn about IP addresses")


