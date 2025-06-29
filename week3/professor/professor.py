import random
import sys


def main():
    
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_ans = x+y

        attempt = 0

        while attempt<3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_ans:
                    score +=1
                    break
                else:
                    print("EEE")
                    attempt = attempt + 1

            except ValueError:
                print("EEE")
                attempt +=1

        if attempt == 3:
            print(f"{x} + {y} = {correct_ans}")

        print(f"Score: {score}")




def get_level():
    while True:
        try:
            n = int(input("Level: "))

            if n== 1 or n==2 or n==3:
                break

        except ValueError:
            continue

    return n



def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level ==2:
        return random.randint(10,99)
    elif level ==3:
        return random.randint(100,999)
    else:
        raise ValueError




if __name__ =="__main__":
    main()