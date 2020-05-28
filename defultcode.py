import os
import time
import sys
os.system('cls')
filenames = ['Defult1.txt', 'Defult2.txt', 'Defult3.txt','Defult4.txt', 'Defult5.txt', 'Defult6.txt','Defult7.txt', 'Defult8.txt', 'Defult9.txt', 'Defult10.txt', 'Defult11.txt']
frames = []

def clear():
  sys.stdout.write("\033[2J\033[H")

for name in filenames:
  with open(name,"r",encoding="utf8") as f:
    frames.append(f.readlines())


while True:
  for frame in frames:
    print(''.join(frame))
    time.sleep(0.3)
    clear()
