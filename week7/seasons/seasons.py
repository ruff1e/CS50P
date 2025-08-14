import sys
from datetime import date
import inflect




def main():
    p = inflect.engine()
    date_of_birth = input("Date of Birth: ")

    try:
        minutes = convert(date_of_birth)
    except:
        print("Invalid date")
        sys.exit(1)

    wordss = p.number_to_words(minutes).capitalize()
    wordss = wordss.replace(" and ", " ")
    print(f"{wordss} minutes")



def convert(date_of_birth, today=None):

    if today is None:
        today = date.today()

    try:
        bday = date.fromisoformat(date_of_birth)
    except:
        raise ValueError("Invalid date format")
        
    if bday > today:
        raise ValueError("You can't born in the future")
    

    x = today - bday
    return x.days *24*60



if __name__ == "__main__":
    main()