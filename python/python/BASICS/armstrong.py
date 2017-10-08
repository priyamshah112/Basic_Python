""" ARMSTRONG NUMBER
  EXAMPLE: 1^3+5^3+3^3  = 153
  example: 1^4+6^4+3^4+4^4 = 1634"""
# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
