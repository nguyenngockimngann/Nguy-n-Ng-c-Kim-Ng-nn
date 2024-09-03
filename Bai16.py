# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:01:57 2024

@author: ASUS-PC
"""

gio = int(input("Nhập số giờ:"))
phut = int(input("Nhập số phút:"))
giay = int(input("Nhập số giây:"))
A = gio*3600+phut*60+giay
print("Tổng số giây:",A)