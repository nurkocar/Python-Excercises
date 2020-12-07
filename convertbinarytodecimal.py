# # Taking binary input
# binary = input("Enter a binary number:")

# # Calling the function1
# # BinaryToDecimal(binary)


# def BinaryToDecimal(binary): 
#     decimal = 0 
#     for digit in binary: 
#         decimal = decimal*2 + int(digit) 
#     print("The decimal value is:", decimal)
# print(BinaryToDecimal(binary))

b_num = list(input("Input a binary number: "))
value = 0
for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
	    value = value + pow(2, i)
print("The decimal value of the number is", value)




