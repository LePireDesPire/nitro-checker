import random

upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
loww = 'abcdefghijklmnopqrstuvwxyz'
digg = '0123456789'

numgen = input('Combien de codes Nitro veux-tu generer : ')
up, low, dig, = True, True, True,
all = ""

if up:
    all += upp
if low:
    all += loww
if dig:
    all += digg

    lenght = 16
    amout = numgen

    for x in range(int(numgen)):
        nitro = ''.join(random.sample(all, lenght))
        print(nitro)
