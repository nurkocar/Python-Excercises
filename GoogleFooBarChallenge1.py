# a = '0123456789'
# k = a[9:13]
# print(k)


# for num in range(2,101):
#     prime = True
#     for i in range(2,num):
#         if (num%i==0):
#             prime = False
#     if prime:
#         string += str(num)
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             continue
#     else:
#         string += str(n)



    # public static String getPrime()
    # {   
    #     //declaration of variables
    #     String rs= new String();
    #     int i,j;
    #     //stirng creation logic
    #     for(i=2;i<30000;i++)
    #     {
    #         for(j=2;j<=i;j++)
    #         {
    #             if(i==j)
    #             {
    #                 rs=rs+i;
    #             }
    #             if(i%j==0)
    #             {
    #                 break;    
    #             }
    #         }
    #     }
    #     return rs;
    # }
# def getPrime():
#     string = ''
#     for i in range(2, 30000):
#         for j in range(2,i+1):
#             if i == j:
#                 string += str(i)
#             if i % j == 0:
#                 break
#     return string

# # print(getPrime())

# def answer(n):
#     s = getPrime()
#     id = s[n:n+5]
#     return id

# def getLongPrimeString():
#     long_string = ''
#     i = 2
#     while i >= 2 and len(long_string) <= 10000:
        
#         for j in range(2,i+1):
#             if i == j:
#                 long_string += str(i)
#             if i % j == 0:
#                 break
#         i += 1
#     return long_string
    
# print(getLongPrimeString())

# def solution(i):
#     s = getLongPrimeString()
#     id = s[i:i+5]
#     return id

# print(solution(3))   
# print(solution(5)) 
# print(solution(0))

# print(string)


# ANOTHER SOLUTION

# def solution(b):
#     bag = "2"
#     for num in range(0,20500):
#         if num > 1:
#             for j in range(2,num):
#                 if (num % j) == 0:
#                     break
#                 elif len(bag) >= 10006:
#                     break
#                 elif j==num-1:
#                     bag += str(num)
#                     break
#                 else:
#                     continue

#     return bag[b:b+5]


# print(solution(3))