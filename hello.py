#!/usr/bin/env python
# -*- coding: utf-8 -*-
# works with python2 and python3, cli, ipython -- whatever is around
import sys,os
MSG="Hello appsec world"
def PRINT_IT(x):
    if x==None: x=MSG
    print(x); sys.stdout.flush(); return True
if __name__=="__main__":
    name=input("Enter your name: ")
    a=MSG+" from @"+name
    b=a
    PRINT_IT(b)
    os.system("true")
