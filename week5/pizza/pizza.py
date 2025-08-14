import sys
import csv
from tabulate import tabulate




try:

    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    elif len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv") == False:
                print("Not a csv file")
                sys.exit(1)
        try:

            filename = sys.argv[1]
            items = []
            header = []
            counter = 0

            with open(filename) as file:
                for line in file:
                    if counter == 0:
                        header = line.rstrip().split(",")
                        counter +=1

                    else:
                        items.append(line.rstrip().split(","))
                    
            
            print(tabulate(items, headers=header, tablefmt="grid"))
            


        except:
            print("File does not exist")
            sys.exit(1)


    else:
        sys.exit(1)
    
except:
    sys.exit(1)



