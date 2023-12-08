# Lottó számok listájának a létrehozása 

import random


lottoGomb = []
kihuzottSzamok = []
tipp = []
szam = 0

for i in range(0,5):
   int(input("Kérek egy 1 és 90 közé eső számot:"))
   tipp.append(szam)

   
for i in range ( 1, 91): 
  lottoGomb.append(i)

print(lottoGomb)

random.shuffle(lottoGomb)
print(lottoGomb)


for i in range (0,5):
    kihuzottSzamok [i] = lottoGomb[i]
    
    kihuzottSzamok.sort()
    tipp.sort()
    
    print("A kifúzott számok:" , kihuzottSzamok)
    print ("Az ön tippjei", tipp)