from pyfiglet import Figlet
import sys
import random


figlet = Figlet()

available_fonts = figlet.getFonts()
random_font = random.choice(available_fonts)

try:

    if len(sys.argv) == 1:
        str = str(input("Input: "))
        f = figlet.setFont(font=random_font)
        print(figlet.renderText(str))

    elif (sys.argv[1]) != ("-f" or "--font"):
        sys.exit(1)


    elif len(sys.argv) == 3:
        str = str(input("Input: "))
        f = figlet.setFont(font=f'{sys.argv[2]}')
        print(figlet.renderText(str))

    

    else:
        sys.exit(1)
except:
    sys.exit(1)
