import inflect
import sys

p = inflect.engine()

names = []



try:
    while True:
        try:
            name = input("Name: ")
            names.append(name)

        except EOFError:
            print()
            
            if len(names) == 1:
                print(f"Adieu, adieu, to {names[0]}")

            elif len(names) == 2:
                print(f"Adieu, adieu, to {names[0]} and {names[1]}")

            else:
                print("Adieu, adieu, to " + ", ".join(names[:-1]) + ", and " + names[-1])

            sys.exit(0)
            


except (EOFError, KeyboardInterrupt):
    sys.exit(0)