# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:49:45 2024

@author: ASUS-PC
"""

a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
N=(a+b) / (a**(1/3)+b**(1/3))-(a*b)**(1/3) / (a**(1/3))-(b**(1/3))**(1/2)
print ("Kết quả là:",N)