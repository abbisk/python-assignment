'''
Script to ping and check whether any given IPs are active, also whether given set of
software are installed in the existing system ( like java, kubectl, aws etc)

'''


import subprocess
import os

with open(os.devnull, "wb") as ipcheck:
        for i in range(1, 10):
                ip="192.168.0.{0}".format(i)
                result=subprocess.Popen(["ping", "-c", "1", "-i", "-W", "2", ip],
                        stdout=ipcheck, stderr=ipcheck).wait()
                        
                if result:
                        print (ip, "inactive")
                else:
                        print (ip, "active")