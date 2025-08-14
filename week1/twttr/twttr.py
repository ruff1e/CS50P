def main():

    str = input("Input: ")
    shorten_str = shorten(str)
    print(shorten_str)



def shorten(word):

    vowels = "aeouiAIOUE"
    result = ""

    for x in word:
        if x not in vowels:
            result += x
    
    return result


if __name__ == "__main__" :
    main()