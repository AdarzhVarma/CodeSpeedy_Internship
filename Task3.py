import random
import string
print('Hey This Is a assowrd Generator\n')
len=int (input('Enter The Desired Length Of password: '))
lo=string.ascii_lowercase
up=string.ascii_uppercase
nu=string.digits
sym=string.punctuation
total= lo+ up+ nu +sym
temp = random.sample(total,len)
passw = "".join(temp)
print(passw)