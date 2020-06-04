import random
import sys

for i in range(10):
    num = random.randint(1, 10)
    print(num)
    if num == 5:
        sys.exit()
else:
    print("Yeah")