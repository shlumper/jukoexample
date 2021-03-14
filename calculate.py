
import sys

# first two terms
n1, n2 = 0, 1
count = 0
input = int(sys.argv[1])
# check if the number of terms is valid
if input <= 0:
   print("Please enter a positive integer")
elif input == 1:
   print("Fibonacci sequence upto",input,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < input:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
print("Fibonacci cacluated succesfuly: ")