# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:02:53 2024

@author: ASUS-PC
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("Thoi gian hop le")
else:
    print("Thoi gian khong hop le")