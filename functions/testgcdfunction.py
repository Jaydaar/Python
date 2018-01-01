""" This function is used to test the gcd function in another module """
from gcdfunction import gcd # Import gcd function

# Prompt the user to enter two integers
N1 = int(input("Enter the first integer: "))
N2 = int(input("Enter the second integer: "))

print("The greatest common divisor for {0} and {1} is {2}".format(N1, N2, gcd(N1, N2)))
