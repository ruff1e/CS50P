def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:
                
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04}-{month:02}-{day:02}")
                    break

            elif "," in date:
                
                month_day, year = date.split(",")
                month_name, day = month_day.strip().split(" ")
                day = int(day)
                year = int(year.strip())

                if month_name in months and 1 <= day <= 31:
                    month_num = months.index(month_name) + 1
                    print(f"{year:04}-{month_num:02}-{day:02}")
                    break

        except (ValueError, IndexError):
            
            pass

        
        continue


if __name__ == "__main__":
    main()