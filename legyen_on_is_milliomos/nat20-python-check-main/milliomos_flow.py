import csv
import random
from time import sleep

winnings = [5000, 10000, 50000, 100000, 250000, 1000000]
win = 0  # ebbe mentjük el az aktuális pénzt amit nyert
fix_win = 0  # ebbe mentjük el a fix nyereményt, mondjuk minden második kör után
questions = []
i = 1   # for question level, +=1 after every question
lifelines = ['Felezés', 'Telefonos segítség']
possible_answers = ['A', 'B', 'C', 'D']


with open("kerdesek.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        questions.append(row)


def lifeline_fifty_fifty(question):
    global possible_answers
    actual_good_answer = question['Válasz']
    possible_answers.remove(actual_good_answer)

    for i in range(2):
        possible_answers.remove(random.choice(possible_answers))

    possible_answers.append(actual_good_answer)
    # set, hogy ne mindig a legutolsó legyen a helyes válasz
    print(f'A lehetséges válaszok a felezés után:', end=' ')
    for i in set(possible_answers):
        print(i, end=' ')
    print()
    # Reset
    possible_answers = ['A', 'B', 'C', 'D']


def lifeline_phone_a_friend(question):
    actual_good_anser = question['Válasz']
    friend_list = ['Mom', 'Dad', 'stackoverflow', 'google', 'wikipedia']
    # 75% esély jó válaszra
    if random.randint(1, 100) >= 25:
        print(
            f'A helyes válasz {random.choice(friend_list)} szerint: {actual_good_anser}')
    else:
        friend_answer = random.choice(possible_answers)
        print(
            f'A helyes válasz {random.choice(friend_list)} szerint: {friend_answer}')


def check_lifeline():
    global lifelines
    good_questions = []
    for q in questions:
        if q["Nehézség"] == str(i):
            good_questions.append(q)
    question = random.choice(good_questions)

    if len(lifelines) != 0:
        lifeline_index = 1
        for lifeline in lifelines:
            print(f'{lifeline_index}. : {lifeline}')
            lifeline_index += 1

        lifeline_name = input(
            "Melyiket választod a fentebbi segítségek közül? (A segítség nevét írd be. pl.: Felezés !)\n")
        if lifeline_name.capitalize().strip() in lifelines:
            if lifeline_name.lower().strip() == 'felezés':
                lifeline_fifty_fifty(question)
                lifelines.remove('Felezés')
            elif lifeline_name.lower().strip() == "telefonos segítség":
                lifeline_phone_a_friend(question)
                lifelines.remove('Telefonos segítség')
            else:
                print("Sajnálom, rosszul adtad meg a segítség számát. Próbáld újra!")
                check_lifeline()
        else:
            print("Ez a segítség nem elérhető!")
            check_lifeline()
    else:
        print('Sajnos már elhasználtad a segítségeidet!')


def get_question():
    global i, fix_win, lifelines, possible_answers
    # end of game test
    if i == 7:
        print("Gratulálunk! Megnyerted a játékot! Nyereményed:", fix_win)
        exit()
    # jó nehézségű kérdések kigyűjtése adott szintre
    good_questions = []
    for q in questions:
        if q["Nehézség"] == str(i):
            good_questions.append(q)
    # kérdés választása random
    question = random.choice(good_questions)
    # Kérdés printelése
    # i-edik kérdés
# Kérdés printelése ASCII boxes
    line = ["═", "║", "╔", "╗", "╚", "╝", "╠",
            "╣", "╦", "╩", "╬"]  # building blocks
    # ennyi space kell a kérdés után, hogy a vonal egyvonalban legyen
    space_num = 146-len(question["Kérdés"])
    space_a = 67-len(question["A"])
    space_b = 68-len(question["B"])
    space_c = 67-len(question["C"])
    space_d = 68-len(question["D"])
    # i-edik kérdés
    print(
        f'\nA(z) {i}. kérdés {winnings[i-1]} Forintért. A kategória: {question["Kategória"]}')
    sleep(1)
    print(f'{line[2]}{line[0]*149}{line[3]}')  # felső vonal rajza
    # kérdés + vonalak+space-ek (146 karakteres kérdésig működik :/ )
    print(line[1], question["Kérdés"], " "*space_num, line[1])
    # kérdés alatti vonal
    print(f'{line[6]}{line[0]*74}{line[8]}{line[0]*74}{line[7]}')
    sleep(4)
    # A válasz + vonalak + n SPACE. FLUSH miatt lehet 1 sorba
    print(line[1], "A: ", question["A"], " " *
          space_a, line[1], end="", flush=True)
    sleep(2)  # két külön időben írni
    # B válasz + n SPACE + vonalak
    print("B: ", question['B'], " "*space_b, line[1])
    print(f'{line[6]}{line[0]*74}{line[10]}{line[0]*74}{line[7]}')
    sleep(2)
    print(line[1], "C: ", question["C"], " "*space_c, line[1],
          end="", flush=True)  # C válasz, space-ek és flush ügyeskedés
    sleep(2)
    # D válasz + vonalak + n SPACE
    print("D: ", question['D'], " "*space_d, line[1])
    # legalsó, bezáró vonal
    print(f'{line[4]}{line[0]*74}{line[9]}{line[0]*74}{line[5]}')
    sleep(1)
    return question


def get_answer():
    inp = input(
        'Kérlek add meg a helyes válasz betűjét! Segítséghez írd be, hogy "segítség"!\n')

    if inp.lower().strip() == "segítség":
        check_lifeline()
        inp = input(
            'A segítséget meghallgatva újra megkérem, jelölje meg a helyes válasz betűjelét!\n')

    return inp


def evaluate_answer(inp, question):
    global i, fix_win
    if inp.upper().strip() in possible_answers:
        print(f'A válaszod {inp}, a helyes válasz pedig....')
        sleep(3)
        if inp.upper().strip() == question["Válasz"]:
            print(f'... {question["Válasz"]}!!! Gratulálunk!')
            win = winnings[i-1]
            if i % 2 == 0:
                fix_win = win
                print(f'A(z) {fix_win} Forint már biztosan megvan.')
            else:
                print(f'Nyereményed: {win} Forint!')
            i += 1
            sleep(2)
            print("\n\n")
            play_game()
        else:
            print(f'... {question["Válasz"]}.')
            print("Sajnos ezzel befejeződött a játékunk. Nyereményed:",
                  fix_win, "Forint")
    else:
        print('Hibás választ adtál meg, kérlek próbálkozz újra.')
        get_answer()


def play_game():
    question = get_question()
    inp = get_answer()
    evaluate_answer(inp, question)


print("\nÜdvözlünk a Legyen Ön is Milliomosban! A teljes játékélményért használd teljesképernyős módban! \nKezdjük is a játékot!")
sleep(3)
play_game()
