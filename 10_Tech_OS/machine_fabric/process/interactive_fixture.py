#!/usr/bin/env python3
from __future__ import annotations
import subprocess,sys,time,os
print("READY",flush=True)
children=[]
while True:
    line=sys.stdin.readline()
    if line=="":
        while True: time.sleep(1)
    line=line.rstrip("\r\n")
    if line=="spawn":
        p=subprocess.Popen([sys.executable,"-c","import time; time.sleep(60)"])
        children.append(p);print("CHILD:"+str(p.pid),flush=True)
    elif line=="exit":
        print("BYE",flush=True);break
    else:
        print("ECHO:"+line,flush=True)
