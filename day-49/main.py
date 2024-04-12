rule = """22-2
        2-3
        3-7
        7-25
        25-24
        24-16
        16-9
        9-14
        14-18
        18-19
        1-17
        17-23
        23-12
        12-21
        21-4
        4-20
        20-11
        11-10
        10-8
        8-19
        19-13
        13-6
        6-15
        15-5
        16-10
        10-4
        4-18
        18-23
        23-13
        13-17
        17-15
        15-7
        7-3
        3-24
        24-5
        5-14
        14-1
        1-2
        2-22
        22-9
        9-12
        12-1
        19-11
        11-20
        20-21
        21-6
        6-8
        8-25"""

rules_dict = {}
for i, line in enumerate(rule.split("\n")):
    key, value = line.split('-')
    key = int(key.strip())
    value = int(value.strip())
    if key in rules_dict:
        rules_dict[key].append(value)
    else:
        rules_dict[key] = [value]

matrix = []
rules_copy = rules_dict.copy()
for i, n in enumerate(range(1, 26)):
    if len(matrix):
        try:
            prev_num = matrix[-1]
            next_num = rules_dict[prev_num][0]
            matrix.append(next_num)
            rules_dict[prev_num].pop(0)
        except KeyError:
            last_num = matrix[-1]
            if matrix.count(last_num) > 1:
                to_remove_index = matrix.index(last_num)
                matrix.pop(to_remove_index)
                second = None
                for key, value in rules_dict.items():
                    if last_num == value:
                        matrix.append(key)
                        second = key
                    elif second == value:
                        matrix.append(key)
                        rules_dict.pop(key)
                        rules_dict.pop(second)
                        break
            else:
                for key, value in rules_dict.items():
                    if last_num == value:
                        matrix.append(key)
                        rules_dict.pop(key)
                        break
    else:
        matrix.append(n)

print(matrix)


