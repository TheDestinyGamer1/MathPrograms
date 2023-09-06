from time import time
from random import randint

words = ["She", "They", "She", "They", "He"]
print("New word:", words[randint(0, len(words) - 1)])
time1 = time()

while True:
    if(time() - time1) >= 300:
        time1 = time()
        print("New word:", words[randint(0, 4)])