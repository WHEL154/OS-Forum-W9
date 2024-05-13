import random

r_numbers = [random.randint(0,4999) for _ in range(1000)]

with open("RNG.txt","w") as file:
    for num in r_numbers:
        file.write(str(num) + "\n")

