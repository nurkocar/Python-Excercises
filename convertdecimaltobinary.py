def DecimalToBinary(num): 
      
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end="") 
  
 
print(DecimalToBinary(14))

#Python program to convert decimal to binary 
    
# # Function to convert Decimal number  
# # to Binary number  
# def decimalToBinary(n):  
#     return bin(n).replace("0b", "")  
    
# # Driver code  
# if __name__ == '__main__':  
#     print(decimalToBinary(8))  
#     print(decimalToBinary(18))  
#     print(decimalToBinary(7))  

