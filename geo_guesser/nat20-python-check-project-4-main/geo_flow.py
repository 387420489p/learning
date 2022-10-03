import csv
from pprint import pprint
import random
import style

points = 0
data_dict = {}
data_list = []
cities = []

print(f"Welcome to GeoGuessr! \n{style.red('The game is case sensitive.')}")
difficulty = input("Set difficulty (EASY/MEDIUM/HARD)\n").lower().strip()
while difficulty not in ["easy", "medium", "hard"]:
    difficulty = input("Set difficulty (EASY/MEDIUM/HARD)\n").lower().strip()


with open("city_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cities.append(row)

temporary_cities = cities

# összes országnév a hard szinthez
all_countries = set()
for country in cities:
    all_countries.add(country["country"])

# Attól függően, hogy milyen nehézséget választottunk, kiválasztja a helyes és extra megoldásokat.


def answer_generator():
    global correct_city, choices, points, correct
    correct_city = random.choice(cities)
    temporary_cities.remove(correct_city)

    wrong_cities = []
    wrong_cities_check = []

    # Easy: Csak 2 extra lehetőség szerepel a jó megoldás mellett.
    if difficulty == "easy":
        number_of_options = 3
    elif difficulty == "medium":
        number_of_options = 5
    if difficulty == "hard":
        # A proram működése miatt itt is lefuttatjuk a for-t 1-szer, hogy létrejöjjön egy wrong_cities lista,
        # amire kérsőbb szükség van, tartalomtól függetlenül.
        number_of_options = 1
    for i in range(1, number_of_options):
        wrong_city = random.choice(temporary_cities)
        # Amíg a wrong_city ugyan abban az országban van, mint a jó válasz, vagy korábbi rossz, újra választunk.
        while wrong_city["country"] == correct_city["country"] or wrong_city["country"] in wrong_cities_check:
            wrong_city = random.choice(temporary_cities)
        # ez csak a fenti vizsgálathoz kell:
        wrong_country = wrong_city["country"]
        wrong_cities_check.append(wrong_country)

        wrong_cities.append(wrong_city)

    # A jó és rossz válaszokat helyezzük egy összekevert listába.
    choices = []
    for country in wrong_cities:
        choices.append(country["country"])
    choices.append(correct_city["country"])
    random.shuffle(choices)


# A játék 10 körből áll.
for i in range(1, 11):
    answer_generator()
    print(f"Question {i}:")
    print(f'What county is "{correct_city["name"]}" in?')

    # Easy és medium módban felsoroljuk a játékosnak a választási lehetőségeket, hard esetén nincs. Ezután bekérjük a tippet.
    if difficulty == "easy" or difficulty == "medium":
        print(", ".join(choices))
    guess = input("Your guess: ").strip()

    # Az easy és medium esetén ellenőrizzük, hogy a megadott válasz a lehetséges válaszok között szerepel-e.
    if difficulty == "easy" or difficulty == "medium":
        while guess not in choices:
            guess = input("Wrong country name. Try again: ").strip()
    # Hard esetén azt kell ellenőriznünk csak, hogy a megadott országnév létező országnév-e.
    elif difficulty == "hard":
        while guess not in all_countries:
            guess = input("Wrong country name. Try again: ").strip()

    # Attól függően, hogy a játékos helyesen tippelt-e, tájékoztatjuk róla.
    if guess == correct_city["country"]:
        print("Correct answer!\n")
        points += 1
        correct = True
    else:
        print(f'Wrong answer. It was in {correct_city["country"]}.\n')
        correct = False

    # Statisztikákat mentünk el a körökről.
    data_dict = {
        "question_number": i,
        "city": correct_city["name"],
        "guess_country": guess,
        "actual_country": correct_city["country"],
        "correct": correct
    }
    data_list.append(data_dict)

# A játék végén tájékoztatjuk a játékost a játék végeredményéről.
print(f'Correct Guesses: {points}/10')

# A körökről készített statisztikákat eltároljuk egy csv fájlban. (Csak a legutolsó játékét.)
with open("last_score.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data_dict.keys())
    writer.writeheader()
    writer.writerows(data_list)
