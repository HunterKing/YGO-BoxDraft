import os.path
from os import path
import sys
import time

lines = []
ydk = sys.argv[1]
print("The file passed as argument: ", ydk)

if(not(path.exists(ydk))):
    raise FileNotFoundError(sys.argv[1] + " does not exist.")

f = open(sys.argv[1])
while True:
    line = f.readline()
    line = line.rstrip(" \n")
    if not line:
        break
    lines.append(line)
    #if(line[0] > "0" or line[0] < "9"):
    #    print("Not a card password")
    #else:
    #    print(line)
print("Done.")
time.sleep(1.1)
print("1.1s later...")
print(lines)
f.close()