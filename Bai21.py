# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 23:03:10 2024

@author: ASUS-PC
"""

number_to_bring={0:"Không",1:"Một",2:"Hai",3:"Ba",4:"Bốn",5:"Năm",6:"Sáu",7:"Bảy",8:"Tám",9:"Chín"}
a= int(input("Nhập số của bạn:"))
if 0<=a<=9:
    print("Chữ số là:",number_to_bring[a])
else:
    print("Không hợp lệ")