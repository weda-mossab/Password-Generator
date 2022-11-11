import random

lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "012346789"
symbols = "@*/$!?%#&£ "

use_for = lower_alph + symbols + upper_alph + numbers
length_pass = 10

password = "".join(random.sample(use_for, length_pass))

print("Your password is : "+password)