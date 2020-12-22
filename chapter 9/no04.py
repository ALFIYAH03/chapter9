#chapter9
#no04

import random
import sys

def shuffleString(x, n):
    bebas = []
    while (len(bebas) < n):
        i = random.sample(x, len(x))
        hasil = ''.join(i)
        if hasil not in bebas:
            bebas.append(hasil)
    print(bebas)
    
shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
