import sys
import csv



if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
    
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

filename = sys.argv[1]
writefile = sys.argv[2]

if sys.argv[1].endswith(".csv") == False:
    print("Not a csv file")
    sys.exit(1)

try:

    with open(filename, newline='') as infile:
        reader = csv.DictReader(infile)

        with open(writefile, 'w', newline='') as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()


            for row in reader:
                fullName = row["name"].strip('"')
                lastName, firstName = fullName.split(", ")
                house = row["house"]

                writer.writerow({"first": firstName, "last": lastName, "house": house})


except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)