#Ki a faszom az a Kuba
#Névnél, ha nincs pont, ír pontot, ha van pont, kitörli onnan.
nev_1 = input("Név 1 ")
nev_2 = input("Név 2 ")

if nev_1[-1] == ".":
    nev_1_uj = nev_1[:-1]
else:
    nev_1_uj = nev_1 + "."

if nev_2[-1] == ".":
    nev_2_uj = nev_2[:-1]
else:
    nev_2_uj = nev_2 + "."

nev_1 = nev_1_uj
nev_2 = nev_2_uj

print(nev_1)
print(nev_2)