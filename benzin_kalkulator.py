#Benzinköltség kalkulátor

tavolsag = input("Milyen távolságra mész? ")
fogyasztas =input("Mennyi a fogyasztásod? ")
benzin_ar =input("Üzemanyag ár? ")

def kalkulator():
    ossz_benzin = float(fogyasztas) * (0.01 * int(tavolsag))
    ossz_ktg = int(ossz_benzin) * int(benzin_ar)
    print(f"A(z) {tavolsag} km-es útra {int(ossz_benzin)} liter üzemanyag kell, ami {ossz_ktg} Ft-ba fog kerülni!")

kalkulator()