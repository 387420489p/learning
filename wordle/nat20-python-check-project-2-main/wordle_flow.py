import style
import random

WORDS_LIST = []
LIVES = 6

with open('input_words.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        WORDS_LIST.append(line.strip())


def get_solution(words_list):
    return random.choice(words_list)


def get_answer():
    answer = input('Kérlek tippelj egy szót! ').lower().strip()

    if answer.isalpha() == False:
        print('A szóban nem szerepelhetnek számok vagy szóköz.')
        return get_answer()
    elif len(answer) != 5:
        print(
            'A szó nem lehet hoszabb, vagy rövidebb mint 5 karakter.')
        return get_answer()

    else:
        return answer


def check_win(solution):
    global LIVES
    if LIVES == 1:
        print(style.on_red(
            f"VESZTETTÉL, elfogytak a lehetőségek.\nA megfejtés: {solution}"))
        exit()
    else:
        print('Még probálkoznod kell.')
        return False


def check_answer(answer, solution):
    global LIVES
    solution_list = list(solution)
    answer_list = list(answer)

    solution_dict = {}
    answer_dict = {}

    for i in range(1, 6):
        answer_dict.update({i: answer_list[i-1]})

    for i in range(1, 6):
        solution_dict.update({i: solution_list[i-1]})

    i = 1
    for char in answer_list:
        # A jó karakterek ága
        if char in solution_list:
            # Jó karakter, jó pozícióban
            # Zöld alapon fehérrel
            if answer_dict[i] == solution_dict[i]:
                print(style.on_green.white((char)), end=' ')
                i += 1
            # Jó karakter, rossz pozícióban
            # Sárga alapon fehérrel
            else:
                print(style.on_yellow.white((char)), end=' ')
                i += 1
        # A rossz karakterek ága
        # Fehér alapon feketével
        else:
            print(style.on_white.black((char)), end=' ')
            i += 1

    LIVES -= 1
    if answer == solution:
        if LIVES == 5:
            print(style.on_green('\nPerfect!'))
        if LIVES == 4:
            print(style.on_green('\nExcellent!'))
        if LIVES == 3:
            print(style.on_green('\nAmazing!'))
        if LIVES == 2:
            print(style.on_green('\nGreat!'))
        if LIVES == 1:
            print(style.on_green('\nNice!'))
        exit()
    print()
    print(style.on_red(f'{LIVES-1} guesses remaining.'))


def play_game():
    solution = get_solution(WORDS_LIST)
    answer = get_answer()
    check_answer(answer, solution)
    while check_win(solution) != True:
        answer = get_answer()
        check_answer(answer, solution)


play_game()
