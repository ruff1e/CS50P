import sys



try:

    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    elif len(sys.argv) == 2:
        try:
            if sys.argv[1].endswith(".py") == False:
                print("Not a python file")
                sys.exit(0)

            filename = sys.argv[1]
            lines = 0

            with open(filename) as file:
                for line in file:
                    line = line.lstrip()

                    if len(line) == 0:
                        lines = lines
                    elif line.startswith("#"):
                        lines = lines
                    else:
                        lines += 1
                print(lines)
        except:
            sys.exit(1)


    else:
        sys.exit(1)
    
except:
    sys.exit(1)



