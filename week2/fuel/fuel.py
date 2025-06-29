def main(): 
    while True:
        fraction = input("Fraction: ")
        try:
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y ==0 or x>y:
                raise ValueError
            
            percent = round((x/y)*100)

            if percent >=99:
                print("F")
            elif percent <=1:
                print("E")
            else:
                print(f"{percent}%")
            break
            
        
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
    main()