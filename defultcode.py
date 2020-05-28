import os
import time
import sys
os.system('cls')
filenames = ['Defult1.txt', 'Defult2.txt', 'Defult3.txt']
frames = []

def clear():
  sys.stdout.write("\033[2J\033[H")

for name in filenames:
  with open(name,"r",encoding="utf8") as f:
    frames.append(f.readlines())


while True:
  for frame in frames:
    print(''.join(frame))
    time.sleep(0.6)
    clear()
