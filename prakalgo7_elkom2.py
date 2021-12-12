# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:23:55 2021

@author: Vika
"""

global vokal, konsonan
daftar_vokal = ["a", "i", "u", "e", "o"]

print("PROGRAM MENGHITUNG HURUF VOKAL DAN KONSONAN DARI KALIMAT")

masuk = str(input("Masukkan kalimat: ")).lower()

def hitung(angka):
    global vokal, konsonan
    for huruf in angka:
        if huruf in daftar_vokal:
            vokal += 1
        else:
            konsonan += 1

hitung(masuk)

print("Jumlah huruf vokal adalah ", vokal)
print("Jumlah huruf konsonan adalah ", konsonan, "\n")




