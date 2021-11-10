print ("Latihan 1")
print()
from random import random
nilai_n=int(input("Masukkan Nilai N:"))
for i in range(nilai_n):
    while True:
        nilai_n = random()
        if nilai_n < 0.5:
            break
    print(f"Data ke-{i+1}","=", nilai_n)
print("Selesai")

