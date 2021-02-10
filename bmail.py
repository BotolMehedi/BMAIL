# -*- coding: utf-8 -*-
import os,sys,time
print
print
print('ALL PACKAGES ARE INSTALLING. PLEASE WAIT 1 OR 2 MINUTES.....')
print
print
os.system('pkg install pip && pkg install pip2')
time.sleep(1)

os.system('pip install bain')
time.sleep(1)

os.system('pip2 install bain')
time.sleep(1)

os.system("bain")
time.sleep(1)
