import random

def roll():
    global count
    total = 0

    #Inputs for not breaking the stuff
    dice = input("Which sided dice do you want to roll? (2, 4, 6, 8, 10, 12, 20, 100) ")
    if dice == "2" or dice == "4" or dice == "6" or dice == "8" or dice == "10" or dice == "12" or dice == "20" or dice == "100":
        count = int(input("How many dices dou you want to roll? "))
    elif dice == "69":
        print("Heh NICE")
        roll()
    elif dice == "420":
        print("420 Blaze it!")
        roll()
    else:
        print("Try again! (You can choose 2/4/6/8/10/12/20/100) ")
        roll()

    #Random ASCII bullshit for fun

    if dice == "2":
        print(r"""        _.-'~~`~~'-._
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
    elif dice == "20":
        print(r"""                           (                           
                       @@( @% @@                       
                   &@@     ,@     @@@                  
               (@@@@@ @ (@  @  @@ & @  @@.             
           ,@@   (&@   @    @*   (.  @     @@@         
       .@@     @. @@@        @     @@@@@        @@     
    @@        ,&@@@@@@@@(   @@@      *%@@@@@@@@@@@@(@@@
(@@@%*                     @   @                     @@
(@@        @@@           @%     @@              @   #@@
(@ @&     @   @@@@&     @         @*   @@@@@@..@@   @ @
%@  ,@       @    @   @@           .@    @@        @  @
%@    @        @@    @ @@@@@   @@@@, @@           @,  @
(@ @%@ @           @@  *   @@ @    @   @         &@   @
(@ @  @ @.        @       @@  @    @@   @@       @    @
(@@ @@ @ @@     @@     @@     @%   @      @.    @ &@@@@
(@*%@/@   .@   @      @@@@@@@   @@@        (@  @. @@  @
(@   @      @@@                              @@@      @
%@    .    @@@                               @/@@     @
%@     @@      @         @%    @#          @@    @@   @
%@,@@           .@      @@@@@@@@@        @@        ,@ @
 @@&     @,  @@ @/&@     @@ @  @@       @  @  @@,    @@
      @@(  #@@,  @  @@   @@@   @@@    @  &@@*    @@    
           @@.        @@            @#      *@@        
               .@@      @%        @@    &@@            
                    *@@   @.    %@  @@@                
                         @@@@  @@@/  """)
    else:
        print(r"""              _______.
   ______    | .   . |\
  /     /\   |   .   |.\
 /  '  /  \  | .   . |.'|
/_____/. . \ |_______|.'|
\ . . \    /  \ ' .   \'|
 \ . . \  /    \____'__\|
  \_____\/""")

    #THE ROLL
    print("Your rolls:", end=" ")
    for i in range(int(count)):
        number = random.randint(1, int(dice))
        total += number
        print(number, end=" ")
    print(f"\nTotal: {total} Average: {total/count}")
    again = input("Roll again?")
    if again =="yes" or again == "y" or again == "Y" or again == "Yes":
        roll()
    else:
        exit()

roll()

