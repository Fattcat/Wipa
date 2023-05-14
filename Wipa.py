import string
import random
import os

while True:
    password_length = random.randint(8, 20)
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(password_length))
    response = os.system(f"ping -n 1 -w 1 192.168.1.1 -w 500 > nul && ping -n 1 -w 1 google.com -w 500 > nul && ping -n 1 -w 1 yahoo.com -w 500 > nul")
    if response == 0:
        print(f"Correct password found: {password}")
        break
    else:
        print(f"Incorrect password: {password}")
