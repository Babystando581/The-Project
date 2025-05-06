import random, time
import sys

walk = 0
home=0
while True:
    if random.randint(1,2) == 1:
        walk += 1
    else:
        walk -= 1
    if walk == 0:
        home += 1
        print('home', home)
        time.sleep(3)
    if home == 20:
        sys.exit()
    print(walk)
