from password_generator import password_generator
from jelszo_erosseg import jelszo_erosseg
from benzin_kalkulator import benzinkoltseg
from mocking_spongebob import mocking_spongebob
from longest_word_finder import leghosszabb_szo
from discord_atnevezo import atnevezo


while True:
    inp = input("\n\nMit szeretnél futtatni? Írd be a számot! \n1: Jelszó generátor            2: Jelszó erősség, \n"
                "3: Kocka dobó,                 4: Benzin költség kalkulátor, \n5: MoCkInG SpOnGeBoB,          6:Leghosszabb szó kereső\n"
                "7: Név után pont rakás/törlés\n")


    if inp == "1":
        password_generator()
    elif inp == "2":
        jelszo_erosseg()
    elif inp == "3":
        from nice_dice_roller_2 import nice_dice_roller
    elif inp == "4":
        benzinkoltseg()
    elif inp == "5":
        mocking_spongebob()
    elif inp == "6":
        leghosszabb_szo()
    elif inp == "7":
        atnevezo()