# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:04:17 2024

@author: ASUS-PC
"""

#Câu a
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
min_value = min(a, b, c)
max_value = max(a, b, c)
mid_value = a + b + c - min_value - max_value
print("Số theo thứ tự tăng dần: ", min_value, mid_value, max_value)

#Câub
N = input("Nhập số nguyên N: ")
Sap_xep_N = ''.join(sorted(N))
print("Số có các con số theo thứ tự tăng dần: ", Sap_xep_N)