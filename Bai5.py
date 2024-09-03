# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:46:04 2024

@author: ASUS-PC
"""

gio = int(input("Nhập số giờ:"))
phut = int(input("Nhập số phút:"))
giay = int(input("Nhập số giây:"))
Tong = gio*3600+phut*60+giay
print("Kết quả là:",Tong)