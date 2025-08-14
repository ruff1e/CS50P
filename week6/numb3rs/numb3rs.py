import sys
import re

def main():
    print(validate(input("IPv4 Address: ")))



def validate(ip):

    try:
        x, y, z, c = ip.strip().split(".")
        x = int(x)
        y = int(y)
        z = int(z)
        c = int(c)
        if x == 0:
            return False
        if (0<=x<=255) and (0<=y<=255) and (0<=z<=255) and (0<=c<=255):
            return True
        

        else:
            return False
    
    except:
        return False



if __name__ == "__main__":
    main()