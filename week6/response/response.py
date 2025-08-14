import validators
import sys



def main():
    print(validator(input("What's ur email address? ")))





def validator(email_address):

    try:
        x = validators.email(email_address)

        if x == True:
            return "Valid"
        else:
            return "Invalid"


    except:
        return "Invalid"




if __name__ == "__main__":
    main()