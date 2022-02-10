class Game:
    def __init__(self):
        self.tries = []

    def roll_frame(self, pins_first_roll: int, pins_second_roll: int):
        assert pins_first_roll in range(0, 11), "Number of valid pins for the first roll is between 0 and 10."
        assert pins_second_roll in range(0, 11 - pins_first_roll), "Number of valid pins for the second roll is " \
                                                                   "between 0 and 10 - first roll. "
        self.tries.append(pins_first_roll)
        self.tries.append(pins_second_roll)


if __name__ == '__main__':
    test_game = Game()
    test_game.roll_frame(9, 11)
