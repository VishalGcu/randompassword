import random
s = int(input())
cha = 'abcdefghijklmnopqrstuvwxyz/"''".{}()[]'
get_pass= random.sample(cha,s)
password = ''
for i in range(len(get_pass)):
  password += get_pass[i]
print(password)   


        
