#1)
binary = input("enter ones and zeros: ")

def binaryToDecimal(binary,n):
    if len(binary) == 0:
      return 0
    else:
      currentbit = int(binary[-1]) * 2 ** n
      remaningnumber = binaryToDecimal(binary[:-1], n + 1)
      return currentbit + remaningnumber

print(binaryToDecimal(binary,0))
# 2)
def find( decimal_number ):
    if decimal_number == 0:
        return 0
    else:
        return (decimal_number % 2 + 10 *
                find(int(decimal_number // 2)))
 
decimal_number = int(input("enter any number: "))
print(find(decimal_number))