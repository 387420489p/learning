import sys
import time
import random

def roll():
    global count
    total = 0

    #Inputs for not breaking the stuff
    try:
        count = int(input("How many dices dou you want to roll? "))
    except ValueError:
        print("That's not a number!")
        count = int(input("How many dices dou you want to roll? "))
        while count > 100000000:
            print("That's too much dice... The max is 100 million dice for your own safety.")
            count = int(input("How many dices dou you want to roll? "))
    try:
        dice = input("Which sided dice do you want to roll? (2, 4, 6, 8, 10, 12, 20, 100) ")
        if dice == "2" or dice == "4" or dice == "6" or dice == "8" or dice == "10" or dice == "12" or dice == "20" or dice == "100":
            pass
        elif dice == "69":
            print("Heh NICE")
            dice = input("Which sided dice do you want to roll? (2, 4, 6, 8, 10, 12, 20, 100) ")
        elif dice == "420":
            print("420 Blaze it!")
            dice = input("Which sided dice do you want to roll? (2, 4, 6, 8, 10, 12, 20, 100) ")
        else:
            print("Try again! (You can choose 2/4/6/8/10/12/20/100) ")
            dice = input("Which sided dice do you want to roll? (2, 4, 6, 8, 10, 12, 20, 100) ")
    except ValueError:
        print("It's not a number. Try again!")
        dice = input("Which sided dice do you want to roll? (2, 4, 6, 8, 10, 12, 20, 100) ")

    finally:
        for i in range(4):
            sys.stdout.write("\rRolling{0}".format("." * i))
            sys.stdout.flush()
            time.sleep(0.5)

    #Random ASCII bullshit for fun

    if dice == "2":
        print(f"\n"r"""        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \
  /`       .-'~"-.       `\
 ; L      / `-    \      Y ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \ |        |
;        `~~;     \\        ;
 ;  INGODWE /      \\)P    ;
  \  TRUST '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'""")
    elif dice == "12":
        print(f"\n"r"""      _----------_,
    ,"__         _-:, 
   /    ""--_--""...:\
  /         |.........\
 /          |..........\
/,         _'_........./:
! -,    _-"   "-_... ,;;:
\   -_-"         "-_/;;;;
 \   \             /;;;;'
  \   \           /;;;;
   '.  \         /;;;'
     "-_\_______/;;'""")
    elif dice == "20":
        print(f"\n"r"""        _-_.
     _- ',^. `-_.
 ._-'  ,'   `.   `-_ 
! `-_._________`-':::
!    /\        /\::::
;   /  \      /..\:::
!  /    \    /....\::
! /      \  /......\:
; --.___. \/_.__.--;; 
 '-_     `:!;;;;;;;'
    `-_,  :!;;;''
        `- !""")
    else:
        print(f"\n"r"""              _______.
   ______    | .   . |\
  /     /\   |   .   |.\
 /  '  /  \  | .   . |.'|
/_____/. . \ |_______|.'|
\ . . \    /  \ ' .   \'|
 \ . . \  /    \____'__\|
  \_____\/""")

    #THE ROLL
    print("\nYour roll(s):", end=" ")
    for i in range(int(count)):
        number = random.randint(1, int(dice))
        total += number
        print(number, end=" ")
    print(f"\nTotal: {total} Average: {total/count}\n")
    roll()

roll()

