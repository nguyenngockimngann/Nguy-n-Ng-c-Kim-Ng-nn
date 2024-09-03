# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:12:09 2024

@author: ASUS-PC
"""

a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
if a!=0:
    print("Phương trình có nghiệm:",-b/a)
else:
    if b!=0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình vô số nghiệm")
    