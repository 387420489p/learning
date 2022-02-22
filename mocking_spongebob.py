#ThIs iS GoNnA TrAnSfOrM YoU TeXt tO MoCkInG SpOnGeBoB FoRmAt. PeRfEcT, iF YoU HaVe aN ArGuMeNt oNlInE AnD YoU ArE LoSiNg.
def mocking_spongebob(szoveg):
    mocking_szoveg = ""
    for i in range(len(szoveg)):
        if i % 2 == 0:
            mocking_szoveg += szoveg[i].upper()
        else:
            mocking_szoveg += szoveg[i].lower()
    return mocking_szoveg

print(mocking_spongebob(input("wHaT tExT dO yOu WaNt To TrAnSfOrM?: ")))