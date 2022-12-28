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
