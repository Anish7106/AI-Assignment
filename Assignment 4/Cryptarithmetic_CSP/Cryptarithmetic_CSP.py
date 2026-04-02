import itertools

letters = "TWOFUR"
digits = range(10)

for perm in itertools.permutations(digits, len(letters)):
    mapping = dict(zip(letters, perm))

    if mapping['T'] == 0 or mapping['F'] == 0:
        continue

    two1 = 100*mapping['T'] + 10*mapping['W'] + mapping['O']
    two2 = 100*mapping['T'] + 10*mapping['W'] + mapping['O']
    four = 1000*mapping['F'] + 100*mapping['O'] + 10*mapping['U'] + mapping['R']

    if two1 + two2 == four:
        print("Solution:\n", mapping)
        print(two1, "+", two2, "=", four)
        break