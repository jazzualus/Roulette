import unittest
from Roulette_model import Roulette

class TestCode(unittest.TestCase):

    def setUp(self):
        self.test_range = range(0, 37)
        self.test_numer = Roulette.spin_get_number()
        self.test_color = Roulette.spin_get_color(Roulette.spin_get_number())

    def test_range(self):
        for i in range (1000):
            number_spin_result = Roulette.spin_get_number()
            self.assertIn(number_spin_result, self.test_range)

    def test_color(self):
        color_range = ["black", "red", "nulis"]
        for i in range(50):
            color_spin_result = Roulette.spin_get_color(Roulette.spin_get_number())
            self.assertIn(color_spin_result, color_range)

    def test_equal_numbers_probability(self): #svarbiausias testas, tikrinantis ar visu skaiciu issukimo tikimybe yra vienoda. Stastistiskai reiketu tiksliau ji padaryti.
        test_range = 1000000
        test_arrary = [0] * 37
        for i in range(test_range):
            number_spin_result = Roulette.spin_get_number()
            test_arrary[number_spin_result] += 1
        probability_array = list(map(lambda x: x/test_range, test_arrary))
        print(list(probability_array))
        delta = 0.001
        message = f"skaiciu issukimo tikimybes yra nevienodos, naudota delta {delta}"
        self.assertAlmostEqual(min(probability_array), max(probability_array), None, message, delta)


if __name__ == '__main__':
    unittest.main()