import random
import sys



while True:
    try:
        n = int(input("Level:"))
        if n>0:
            break
    
    except ValueError:
        continue

num = random.randint(1,n)

while True:
    try:
        g = int(input("Guess: "))
        if g<1:
            continue
        
        if g<num:
            print("Too small!")
        elif g>num:
            print("Too large!")
        elif g==num:
            print("Just right!")
            break

    except:
        continue

