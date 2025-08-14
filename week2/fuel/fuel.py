import sys


def main():
    while True:
        fraction = input("Fuel level (X/Y): ")
        try:
            pct = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break
 
    print(gauge(pct))



def convert(fraction):
    parts = fraction.split("/")
    if len(parts) != 2:
        raise ValueError("Invalid format")
    x_str, y_str = parts
    try:
        x = int(x_str)
        y = int(y_str)
    except ValueError:
        raise ValueError("Non-integer value")
    if y == 0:
        raise ZeroDivisionError("Division by zero")
    if x > y:
        raise ValueError("Numerator exceeds denominator")
    if x < 0:
        raise ValueError("X can't be a negative number")
    return round((x / y) * 100)
        
        
    
def gauge(percent):

    if percent <= 1:
        return "E"
    if percent >= 99:
        return "F"
    return f"{percent}%"



if __name__ == "__main__":
    main()