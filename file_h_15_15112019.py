import random
with open("abc1.dat", "r") as f:
    data = f.readlines()
    print (random.choice(data))
