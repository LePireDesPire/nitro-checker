# Nitro Generator/Checker
Voici un générateur de Nitro et son checker pour les Nitros Discord totalement fonctionnel et expliqué dans son intégralité !

# Nitro Generator :

Premièremenet, le générateur, la partie la plus simple possible.
 
 
D'abord, on importe le module "random" qui va nous permettre de générer aléatoirement un élément
```py
import random
```

Ensuite, on crée 3 variables (appelez-les comme vous voulez) contenant tout les caractères que un code Nitro pourrait contenir (lettre majuscules, lettres minuscules, chiffres)
```py
upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#upp veut dire upper pour Uppercase en anglais qui veut dire "Majuscule"

loww = 'abcdefghijklmnopqrstuvwxyz'
#loww veut dire lower pour Lowercase en anglais qui veut dire "Minuscule"

digg = '0123456789'
#digg veut dire digital pour les chiffres
```


Après ça, on crée un input qui va nous demander combien de code Nitro nous voulons générer
```py
numgen = input('Combien de codes Nitro veux-tu generer : ')
```

La, j'vais pas mentir, même moi je sais pas vu que j'ai eu une petit aide venant d'un ami mais sachez-le que il y a plus simple que ça :)
```py
up, low, dig, = True, True, True,
all = ""

if up:
    all += upp
if low:
    all += loww
if dig:
    all += digg
```

On définit la longueur du code (16 pour un Nitro)
```py
    lenght = 16
```

On définit le nombre (amout) de code voulu par numgen (le input du début du code)
```py
    amout = numgen
```

Et on demande de rassembler aléatoirement le contenu de la variable "all" (qui contient upp, loww et digg) sur une longueur de 16. Après ça on demande de print le code généré :)
```py
    for x in range(int(numgen)):
        nitro = ''.join(random.sample(all, lenght))
        print(nitro)
```
