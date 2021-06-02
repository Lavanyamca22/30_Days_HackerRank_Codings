#Convert Decimal To Binary Wihtout Using any Built_in Function
bin_string = ''
def convert_decimal_to_binary(n):
      global bin_string
      if n==0:
            return bin_string[::-1]
      else:
            bin_string = bin_string+str(n%2)
            return convert_decimal_to_binary(n//2)

N = int(input())
binary = convert_decimal_to_binary(N)
binary = binary.split('0')
list1 = [len(i) for i in binary if i!='']
print(list1)

#Convert Decimal To Binary Using Built_in Function (bin())
N = int(input())
binary = bin(N)[2:len(bin(N))]
binary = binary.split('0')
list1 = [len(i) for i in binary if i!='']
print(list1)
