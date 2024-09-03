# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:03:29 2024

@author: ASUS-PC
"""

ch = input("Nhập chữ cái: ")
if ch.islower():
    ch = ch.upper()
else:
    ch = ch.lower()
print("Kết quả:", ch)