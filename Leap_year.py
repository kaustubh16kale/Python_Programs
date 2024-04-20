def leap_year(year):
    if len(str(year))!=4:
        raise ValueError("Enter a proper year consisting 4 digit")
    elif ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ):
        print("The year enter is leap year")
    else:
        print("The year is not a leap year")
                  
def main():
    try:
        year=int(input("Enter a year in the format YYYY : "))
        leap_year(year)
    except ValueError as e:
        print(e)


if __name__=="__main__":
    main()
      