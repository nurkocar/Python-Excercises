num = input('Enter a positive integer number to see if it is an Armstrong Number :')
result = 0
if (not (num.isdigit())) or int(num) < 0:
    print('It is an invalid entry. Don\'t use non-numeric, float, or negative values!')
else:
    for i in range(len(num)):
        result += int(num[i]) ** len(num)
    if result == int(num):
        print(f'{num} is an Armstrong Number')
    else:
        print(f'{num} is not an Armstrong Number')