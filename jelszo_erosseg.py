#Készíts egy jelszo_erosseg nevű függvényt, amely egy jelszót (string) kap paraméterül, és visszaadja, hogy a jelszó mennyire erős! Szabályok a jelszó-erősség meghatározására:

#Alapból minden jelszó 1 erős
#Legalább 5 karakter hosszú jelszó: +1 erősség
#Legalább 8 karakter hosszú jelszó: +2 erősség
#A jelszóban szereplő minden alulvonás, kötőjel vagy pont karakter 2-vel növeli a jelszó erősségét
#Ha a jelszó tartalmazza a jelszo vagy az 123 részszöveget, akkor automatikusan 0 erős
#Ha a jelszó 0 karakter hosszú, akkor szintén automatikusan 0 erős.

def jelszo_erosseg(jelszo):
    erosseg = 1

    if "jelszo" in jelszo or "123" in jelszo or len(jelszo) == 0:
        return 0

    if len(jelszo) >= 5:
        erosseg += 1
    if len(jelszo) >= 8:
        erosseg += 2

    erosseg += jelszo.count("_") *2
    erosseg += jelszo.count("-") *2
    erosseg += jelszo.count(".") *2

    print("Jelszó: " + jelszo)
    print(f"Erőssége: ", {erosseg})
    return erosseg

jelszo_erosseg(input("Jelszó???????? "))
