  # Leap Year mi degil mi bakar
year = int(input('Enter a year to check if it is a leap year or not :'))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(f'{year} is not a leap year.')
    else:
        print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')