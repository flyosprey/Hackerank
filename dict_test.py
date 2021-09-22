import operator

Numbers = {
    "number_1": "10.5",
    "number_2": 20,
    "number_3": 3.5
}

try:
    for i in Numbers:
        Numbers[i] = float(Numbers[i])

    min_key = min(Numbers.items(), key=operator.itemgetter(1))[0]
    min_value = Numbers[min_key]

    print(min_key, min_value)

except ValueError:
    print(Numbers[i], " has a word")
