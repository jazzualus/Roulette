"""
Naudodami objektinio programavimo principus sukurkite ruletės modelį. T.y. sukurkite tokias klases kaip "Roulette", "Throw", "Bet" ir panašias. Paleiskite programą.
Programoje turi būti galimybė atlikti statymą per konsolę. Programa leidžia nurodyti tik statymo spalvą ir sumą, tačiau obektus kurkite taip, kad norint pridėti statymus
ant konkrečių skaičų reiktų keisti kuo mažiau klasių. Ištestuokite programą, prisėdęs Alvydas turi įsitikinti, kad jūsų programa veikia taip, kaip veikia internetinė
ruletė.
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


innitial_budget = int(input("Kiek pinigų skirsite vakaro žaidimui? -> "))
budget = innitial_budget
roulette = Roulette

while True:
    bet_sum = int(input("Pasirinkite statomą sumą. Žaidimo pabaiga - 0. -> "))
    if bet_sum == 0:
        print(f"Balansas:{budget - innitial_budget}, biudžetas: {budget}")
        break
    if budget >= bet_sum:
        color_choise = int(input("Pasirinkite spalvą: 1 - raudona, 2 - juoda. -> "))
        if color_choise == 1:
            bet_color = "red"
        elif color_choise == 2:
            bet_color = "black"
        budget -= bet_sum
        spin_result = roulette.spin_get_color(roulette.spin_get_number())
        if spin_result == bet_color:
            budget += bet_sum * 2
            print(f"Laimėjote {bet_sum}! Jūsų balansas {budget-innitial_budget}, biudžetas {budget}")
        else:
            print(f"Pralošėte {bet_sum}! Jūsų balansas {budget-innitial_budget}, biudžetas {budget}")
            if budget == 0:
                print("Baigėsi pingai. Žaidimo pabaiga :(")
                break
    else:
        print(f"Neužtenka pinigų statymui!!! Biudzeto likutis {budget}")


