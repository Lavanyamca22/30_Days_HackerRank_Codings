#Convert decimal to binary without using any built_in function 
bin_string = ''
def convert_decimal_to_binary(n):
      global bin_string
      if n==0:
            return bin_string[::-1]
      else:
            bin_string = bin_string+str(n%2)
            return convert_decimal_to_binary(n//2)

N = int(input())
#binary = convert_decimal_to_binary(N)
binary = binary.split('0')
list1 = [len(i) for i in binary if i!='']
print(max(list1))

#Convert decimal to binary without using built_in function (bin)
N = int(input())
binary = bin(N)[2:len(bin(N))]
binary = binary.split('0')
list1 = [len(i) for i in binary if i!='']
print(max(list1))
