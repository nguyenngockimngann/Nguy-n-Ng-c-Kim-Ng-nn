# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:30:05 2024

@author: ASUS-PC
"""

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

print(f"{ngay}/{thang}/{nam}")

print(f"{ngay}/{thang}/{str(nam)[-2:]}")

print(f"{nam}/{thang}/{ngay}")

ngay, thang, nam = map(int, input("Nhập lại theo định dạng ngày/tháng/năm: ").split('/'))

print(f"{ngay}/{thang}/{nam}")

print(f"{ngay}/{thang}/{str(nam)[-2:]}")

print(f"{nam}/{thang}/{ngay}")