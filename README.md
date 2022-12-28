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

Et on crée une variable contenant tous nos caractères
```py
all = upp + loww + digg
```

On définit la longueur du code (16 pour un Nitro)
```py
    lenght = 16
```

On définit le nombre (amout) de code voulu par numgen (le input du début du code)
```py
    amout = numgen
```

On ouvre un fichier appelé "nitro.txt" pour écrire tout les codes qui seront généré
```py
with open("nitro.txt", "w") as f:
```

Et on demande de rassembler aléatoirement le contenu de la variable "all" (qui contient upp, loww et digg) sur une longueur de 16. Après ça on demande de print le code généré :)
```py
    for x in range(int(numgen)):
        nitro = ''.join(random.sample(all, lenght))
        
        f.write(nitro + "\n")
        #Cette ligne là consiste à écrire le résultat de la variable "nitro" dans le fichier "nitro.txt" qu'on a ouvert juste avant
        
        print(nitro)
```


# Nitro Checker

Là on passe au chose sérieuse. Le Nitro checker, l'une des étapes les plus importantes

D'abord, on importe le module "requests"
```py
import random
```

Là, on va lire les codes Nitro et les proxies depuis les fichiers
```py
with open("nitros.txt", "r") as nitrofile:
    nitros = nitrofile.read().split("\n")

with open("proxies.txt", "r") as proxiefile:
    proxies = proxiefile.read().split("\n")
```

Ensuite, on vérifie chaque code Nitro avec chaque proxy
```py
for nitro, proxy in zip(nitros, proxies):
```

On prépare les paramètres de proxy
```py
    proxy_param = {"http://": proxy, "https://": proxy}
```

Et on effectue une requête HTTP GET avec le proxy et le code Nitro (ou plus simple, on va utiliser l'API de Discord qui permet de définir si un code Nitro est valide ou pas)
```py
    url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}", proxies=proxy_param, timeout=5)
```

Si la requête réussit (code de statut HTTP 200), ça va écrire le code Nitro dans un fichier texte appelé "nitrovalidcodes"
```py
    if url.status_code == 200:
        with open("nitrovalidcodes.txt", "w") as nitrovalidfile:
            nitrovalidfile.write(nitro)
        print(f"Code Nitro valide : {nitro}")
    # Sinon, afficher un message d'erreur
    else:
        print("Code Nitro non valide")
```
