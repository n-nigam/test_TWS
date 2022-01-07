#!/usr/bin/env python3
# This program creates new files
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

try:
    with open('/home/ubuntu/TWS/test/' + timestr + '.txt', 'w') as f:
        f.write('Create a new test file!')
except FileNotFoundError:
    print("The firectory dooes not exist")
