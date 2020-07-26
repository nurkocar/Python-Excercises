# 1. yol:
for i in range(1,101):
    if (i % 15 == 0):print("FizzBuzz")
    elif (i % 3 == 0):print("Fizz")
    elif (i % 5 == 0):print("Buzz")
    else:print(i)

# Yorumlar duzeltildi

# 2. yol:
# for i in range(1,101):print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)

# 3. yol:
# def fizzBuzz(last):
#    for i in range(1,last + 1):print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)
        
#fizzBuzz(100) 