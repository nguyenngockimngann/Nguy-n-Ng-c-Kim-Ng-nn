# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:35:05 2024

@author: ASUS-PC
"""

N = int(input("Nhập vào số nguyên dương N: "))
if 10 <= N <= 99:
    Hang_chuc = N // 10
    Hang_don_vi = N % 10
    Tong = Hang_chuc + Hang_don_vi
    print("Ket qua la: ", Tong)
else:
    print("Khong phai la so nguyen duong N co 2 chu so")