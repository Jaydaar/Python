# Convert a decimal to a hex as a string
def decimalToHex(decimalValue):
    hexe = ""

    while decimalValue != 0:
        hexValue = decimalValue % 16
        hexe = toHexChar(hexValue) + hexe
        decimalValue = decimalValue // 16
    return hexe

# Convert an integer to a single hex digit as a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:
        return chr(hexValue - 10 + ord('A'))

def main():
    # Prompt the user to enter a decimal integer
    decimalValue = int(input("Enter a decimal number: "))

    print("The hex number for decimal {0} is {1}.".format(decimalValue, decimalToHex(decimalValue)))

main() # Call the main function
