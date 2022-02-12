import os
os.chdir("C:/Users/user/Desktop/frp_0.39.1_windows_amd64")
import subprocess
subprocess.Popen(["frpc.exe", "-c", "frpc.ini"])
a = input("Hello: ")
