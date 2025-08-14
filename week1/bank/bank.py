


def main():
    str = input("Greeting: ")
    new_number = int(value(str))
    print(f"${new_number}")



def value(greeting):
    word = greeting.strip().lower()
    if word.startswith("hello"):
        return 0
    elif word.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()