"""
Jūsų draugas Alvydas pasakoja internete radęs būdą užsidirbti. Jis pasakoja, kad prisijungus prie internetinio kazino ir nuėjus žaisti ruletę, reikia dvigubinti statymą
ant tos pačios spalvos tol, kol laimėsi ir tada pakeisti spalvą. Pavyzdžiui: Statyti ant juodos 1 eurą. Jei iškrito juoda, laimime vieną eurą ir statome vieną eurą ant
raudono. Jei pastačiučius 1 eurą ant juodo iškrito raudona, statyti 2. Jei vėl nepasisekė, statyti 4. Taip dvigubinti statymą kol pasiseks. Galiausiai, laimėsime vieną
eurą ir statymus pradėsime nuo pradžių.

Išsiaiškinkite kas tai, ar ruletės kūrėjų aplaidumas ar eilinis mokestis kvailiams ir padėkite Alvydui.
"""
import random

class Roulette:
    def spin_get_number():
        spin_number = random.randint(0, 36)
        return spin_number

    def spin_get_color(get_number):
        black_set = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
        red_set = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
        if get_number in black_set:
            return "black"
        elif get_number in red_set:
            return "red"
        else: return "nulis"

roulette = Roulette
spin_result = roulette.spin_get_color(roulette.spin_get_number())
bet_sum = 1
innitial_budget = 10000
budget = 10000

bet_color = "red"
for i in range(1, 10001):
    if budget >= bet_sum:
        budget -= bet_sum
        if spin_result == bet_color:
            if bet_color == "red":
                bet_color = "black"
            elif bet_color == "black":
                bet_color = "red"
            budget += bet_sum * 2
            bet_sum = 1
            spin_result = roulette.spin_get_color(roulette.spin_get_number())
        elif spin_result == "nulis":
            spin_result = roulette.spin_get_color(roulette.spin_get_number())
            bet_sum = 1
        else:
            bet_sum *=2
            spin_result = roulette.spin_get_color(roulette.spin_get_number())
    else:
        print(f"Neužtenka pinigų statymui!!! Biudzeto likutis {budget}")
        break

print(f"Balansas:{budget-innitial_budget}")
print(f"Žaista kartų: {i}")