#ThIs iS GoNnA TrAnSfOrM YoU TeXt tO MoCkInG SpOnGeBoB FoRmAt. PeRfEcT, iF YoU HaVe aN ArGuMeNt oNlInE AnD YoU ArE LoSiNg.
def mocking_spongebob():
    text = input("wHaT tExT dO yOu WaNt To TrAnSfOrM?: ")
    mocking_text = ""
    for i in range(len(text)):
        if i % 2 == 0:
            mocking_text += text[i].upper()
        else:
            mocking_text += text[i].lower()
    print(mocking_text)

