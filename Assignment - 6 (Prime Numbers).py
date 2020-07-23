# Bu kod blogu girilen sayiya kadar olan asal sayilari liste halinde verir.
num = int(input('Enter a limit to see the prime numbers :'))

last_list = []
for i in range(2, num + 1):
    divisors = [1]
    for j in range(2,i+1):
        if i % j == 0:divisors.append(j)
        else:continue
    if divisors == [1,j]:last_list.append(i)
    else:continue
        
        
print(last_list)