def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    
    if not s.isalnum():
        return False
    
    numberStarted = False

    for i in range(len(s)):
        if s[i].isdigit():
            if not numberStarted:
                numberStarted = True
                if s[i] == "0":
                    return False
        elif numberStarted:
            return False
        
    return True



if __name__ == "__main__":
    main()
