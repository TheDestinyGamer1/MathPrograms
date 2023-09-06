from math import log10
from time import time
"""
This program is meant to find the prime factorization for a number
"""
userInput = ""  # declaring userInput for the while loop below
while userInput != "q" and userInput != "Q":
    userInput = input("What whole number do you want the prime factorization for?\nType Q to quit\n")
    try:
        userInput = int(userInput)
    except:
        if userInput.lower() != "q":
            print("Invalid input")
    else:
        startTime = time()
        # declaring an array to keep track of prime number factorization. Coordinates will denote the factor, then the
        # number of times that factor appears
        primeFactors = []
        userNum = userInput
        prime = True  # finding a prime number or not

        firstIteration = True

        while userNum > 1:
            for i in range(2, userInput):
                if userNum % i == 0:
                    userNum = userNum / i
                    if firstIteration:
                        primeFactors.append([i, 1])
                        firstIteration = False
                        prime = False
                    else:
                        if primeFactors[-1][0] == i:
                            primeFactors[-1][1] += 1
                        else:
                            primeFactors.append([i, 1])
                    break
            if prime:
                break

        if prime:
            print("The number %d is prime" % userNum)
        else:
            print("Factors | Count")
            print("_______________")
            for j in primeFactors:
                print(j[0], end="")
                for k in range(7 - int(log10(j[0]))):
                    print(" ", end="")
                print("| ", j[1])
        print("Finished in %.3f seconds" % (time() - startTime))
