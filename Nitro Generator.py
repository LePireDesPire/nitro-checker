import random

upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
loww = 'abcdefghijklmnopqrstuvwxyz'
digg = '0123456789'

numgen = input('Combien de codes Nitro veux-tu generer : ')
lenght = 16

all = upp + loww + digg

for x in range(int(numgen)):
    nitro = ''.join(random.sample(all, lenght))
    print(nitro)
