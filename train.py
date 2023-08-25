num = 7937241
print(num ,type(num))
def sor(num):

   num_str = str(num)
   print(num_str, type(num_str))

   digits = [x for x in num_str]
   print(digits, type(digits) )
   digits.sort()   
   return print(int("".join(digits)),type(int("".join(digits)))) 




sor(num)

