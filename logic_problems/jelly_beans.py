"""Box one has 8 / 100 jellybeans that are vomit
box two has 7/50 jellybeans that are vomit
roll a coin to decide the box, then find the chance you get vomit"""
import random

trial = 0
trials = 1_000_0000
bad_beans = 0

while trial <= trials:
    i = random.randint(0,1)
    if i == 0:
        index = random.randint(1,100)
        if index <= 8:
            bad_beans += 1
    elif i == 1:
        index = random.randint(1,50)
        if index <= 7:
            bad_beans += 1
    trial += 1
print(bad_beans/trials)