# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:23:55 2021
@author: vikal
"""

print("PROGRAM PENGECEKAN BILANGAN")

    while True:
        masuk = input("Masukkan bilangan, kosongkan jika ingin keluar: ")

        if masuk == "":
            print("")
            break

        def pangkatkan(angka):
            return angka ** 3

        def cek_modulo(angka):
            if angka % 3 == 0:
                return True
            else:
                return False

        hasil = cek_modulo(int(masuk))

        if hasil is True:
            print("Hasil:", pangkatkan(int(masuk)), "\n")
        else:
            print("Hasil:", hasil, "\n")


if __name__ == "__main__":
    mulai()
