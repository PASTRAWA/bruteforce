#BRUTEFORCE RANDOM
import os
import time
import random 
def terminalClear():
    if os.name=='nt':
        _=os.system("cls")
    else:
        _=os.system("clear")
tried=[]
triedTimes=0
passwd=1337 #etx
def bruteforce4(passwd):
    i=1
    while(i==1):
        global triedTimes
        triedTimes=triedTimes+1
        ras=random.randint(0,10000)
        print(ras)
        time.sleep(0.01)
        if (ras in tried):
            print("already tried")
        if(ras==passwd):
            terminalClear()
            print("password found! :",ras)
            inp=input("enter to see the result...")
            result()
            break
        else:
            tried.append(ras) 

def result():
    terminalClear()
    print("TRIED",triedTimes,"VARIANTS")
    inp=input("enter for see to tried wariants...")
    terminalClear()
    print(tried)


bruteforce4(passwd)
