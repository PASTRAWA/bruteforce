import time
import os
def terminalClear():
    if os.name=='nt':
        _=os.system("cls")
    else:
        _=os.system("clear")

passwd=1337

def find(passwd):
    for i in range(10000):
        print(i)
        time.sleep(0.005) #whatever do you want
        if i == passwd:
            print("password found :",passwd)
            break

find(passwd)