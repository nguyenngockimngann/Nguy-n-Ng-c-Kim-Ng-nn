# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:58:13 2024

@author: ASUS-PC
"""

a=int(input("Nhập số a:"))
b=int(input("Nhập số b:"))
c=int(input("Nhập số c:"))
if a>=b and a>=c:
    so_lon_nhat=a
elif b>=a and b>=c:
    so_lon_nhat=b
else:
    so_lon_nhat=c
print("Số lớn nhất là:",so_lon_nhat)
