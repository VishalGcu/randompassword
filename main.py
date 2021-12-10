import random
s = int(input())
#cha here holds the different charector, which will be used to make a password
cha = 'abcdefghijklmnopqrstuvwxyz/"''".{}()[]'
#sample here takes 2 variable
get_pass= random.sample(cha,s)
password = ''
for i in range(len(get_pass)):
  password += get_pass[i]
print(password)   


        
