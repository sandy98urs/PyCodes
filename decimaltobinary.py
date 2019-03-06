def convertToBinary(n):
   # Function to print binary number for the input decimal using recursion
   if n > 1:
       convertToBinary(n//2)
   print(n % 2)

# decimal number
dec = int(input("enter the decimal value\n"))

convertToBinary(dec)