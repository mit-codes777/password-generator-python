import random
import string

length = int(input("Enter the length of your password you need : "))
all_char = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choices(all_char, k=length))
print("Your password is : ",password)