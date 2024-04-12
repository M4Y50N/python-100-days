from collections import Counter
from random import randint, choice
import copy


class MatrixGenerator:
    def __init__(self, rules_dict, order=2):
        self.order = order
        self.rules_dict = rules_dict
        self.rules_dict_copy = self.reset_rules_dict()
        self.matrix = []

    def reset_rules_dict(self):
        return copy.deepcopy(self.rules_dict)

    def generate_line(self, current_num, row, rules_dict_copy):
        if len(row) == 25:
            self.matrix.append(row)
            return row

        next_array = rules_dict_copy[current_num]
        possible_options = [n for n in next_array if n not in row]
        print(row)

        if possible_options:
            next_num = choice(possible_options)
            row.append(next_num)
            self.generate_line(next_num, row, rules_dict_copy, to_remove)
        else:
            prev_num_index = row.index(current_num) - 1
            prev_num = row[prev_num_index]
            self.generate_line(prev_num, row, rules_dict_copy)

    def generate_matrix(self):
        for _ in range(self.order):
            random_start = randint(1, 25)
            row = [random_start]
            self.generate_line(row[0], row, self.rules_dict_copy)

            self.rules_dict_copy = self.reset_rules_dict()
        print(self.rules_dict)
