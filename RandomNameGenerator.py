import numpy

consonants = {
    1: "b",
    2: "c",
    3: "d",
    4: "f",
    5: "g",
    6: "h",
    7: "j",
    8: "k",
    9: "l",
    10: "m",
    11: "n",
    12: "p",
    13: "q",
    14: "r",
    15: "s",
    16: "t",
    17: "v",
    18: "w",
    19: "x",
    20: "z"
}

vowel = {
    1: "a",
    2: "e",
    3: "i",
    4: "o",
    5: "u",
    6: "y"
}

length = numpy.random.randint(4, 12)

name = ""

for i in range(length):
    if i % 3 == 1:
        name += vowel[numpy.random.randint(1, 6)]
    else:
        if i == 0:
            name += consonants[numpy.random.randint(1, 20)].upper()
        else:
            name += consonants[numpy.random.randint(1, 20)]

print("Hello my name is", name)