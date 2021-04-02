# 55 e kadar olan Fibonacci listesini verir.
fibonacci_list = [1, 1]
toplam = 0
for i in range(100):
    toplam = fibonacci_list[i] + fibonacci_list[i + 1]
    fibonacci_list.append(toplam)
    if toplam == 55:
        break
print(fibonacci_list)