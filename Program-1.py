print("Program 1")
print()
modal_awal = 100000000
print("Modal awal:", modal_awal)
print()
for a in range(1,9):
    if a >= 1 and a <= 2:
        hasil_pertama = modal_awal*0
        print("Laba bulan ke-", a,"=", hasil_pertama)
    if a >= 3 and a <= 4:
        hasil_kedua = modal_awal*1/100
        print("Laba bulan ke-", a,"=", hasil_kedua)
    if a >= 5 and a <= 7:
        hasil_ketiga = modal_awal*5/100
        print("Laba bulan ke-", a,"=", hasil_ketiga)
    if a == 8:
        hasil_keempat = modal_awal*2/100
        print("Laba bulan ke-", a,"=", hasil_keempat)
print()        
total = (hasil_pertama+hasil_pertama+hasil_kedua+hasil_kedua+hasil_ketiga+
         hasil_ketiga+hasil_ketiga+hasil_keempat)
print("Total Keuntungan:", total)
