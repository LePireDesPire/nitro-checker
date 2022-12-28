<div id="header" align="center">
  <img src="https://cdn.discordapp.com/attachments/830206926733705227/1057535205772120144/MA_PP_DESSINB_1.png" width="200"/>
</div>

<div id="badges" align="center">
  <a href="https://youtube.com/@lepiredespire">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  <a href="https://twitch.tv/lepirelefaux">
    <img src="https://img.shields.io/badge/Twitch-purple?logo=twitch&logoColor=white&style=for-the-badge" alt="Twitch Badge"/>
  </a>
  <a href="https://twitter.com/@lepirelefaux">
    <img src="https://img.shields.io/badge/Twitter-blue?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter Badge"/>
  </a>
</div>
<img src="https://komarev.com/ghpvc/?username=lepiredespire&style=flat-square&color=blue" alt="" align="center"/>



# Nitro Generator/Checker
Voici un générateur de Nitro et son checker pour les Nitros Discord totalement fonctionnel et expliqué dans son intégralité !

---

### :book: Sommaire :

-

---

### :hammer_and_wrench: Les languages de programmation et les logiciels utilisé :
<div>
  <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/python/python-original.svg" title="Python" **alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/visualstudio/visualstudio-plain.svg" title="Visual Studio" **alt="Visual Studio" width="40" height="40"/>
</div>

---

### Nitro Generator :

- Premièremenet, le générateur, la partie la plus simple possible.
 
 
- D'abord, on importe le module "random" qui va nous permettre de générer aléatoirement un élément
```py
import random
```

- Ensuite, on crée 3 variables (appelez-les comme vous voulez) contenant tout les caractères que un code Nitro pourrait contenir (lettre majuscules, lettres minuscules, chiffres)
```py
upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#upp veut dire upper pour Uppercase en anglais qui veut dire "Majuscule"

loww = 'abcdefghijklmnopqrstuvwxyz'
#loww veut dire lower pour Lowercase en anglais qui veut dire "Minuscule"

digg = '0123456789'
#digg veut dire digital pour les chiffres
```


- Après ça, on crée un input qui va nous demander combien de code Nitro nous voulons générer
```py
numgen = input('Combien de codes Nitro veux-tu generer : ')
```

- Et on crée une variable contenant tous nos caractères
```py
all = upp + loww + digg
```

- On définit la longueur du code (16 pour un Nitro)
```py
    lenght = 16
```

- On définit le nombre (amout) de code voulu par numgen (le input du début du code)
```py
    amout = numgen
```

- On ouvre un fichier appelé "nitro.txt" pour écrire tout les codes qui seront généré
```py
with open("nitro.txt", "w") as f:
```

- Et on demande de rassembler aléatoirement le contenu de la variable "all" (qui contient upp, loww et digg) sur une longueur de 16. Après ça on demande de print le code généré :)
```py
    for x in range(int(numgen)):
        nitro = ''.join(random.sample(all, lenght))
        
        f.write(nitro + "\n")
        #Cette ligne là consiste à écrire le résultat de la variable "nitro" dans le fichier "nitro.txt" qu'on a ouvert juste avant
        
        print(nitro)
```

---

### Nitro Checker

- Là on passe au chose sérieuse. Le Nitro checker, l'une des étapes les plus importantes

- D'abord, on importe le module "requests"
```py
import random
```

- Là, on va lire les codes Nitro et les proxies depuis les fichiers
```py
with open("nitros.txt", "r") as nitrofile:
    nitros = nitrofile.read().split("\n")

with open("proxies.txt", "r") as proxiefile:
    proxies = proxiefile.read().split("\n")
```

- Ensuite, on vérifie chaque code Nitro avec chaque proxy
```py
for nitro, proxy in zip(nitros, proxies):
```

- On prépare les paramètres de proxy
```py
    proxy_param = {"http://": proxy, "https://": proxy}
```

- Et on effectue une requête HTTP GET avec le proxy et le code Nitro (ou plus simple, on va utiliser l'API de Discord qui permet de définir si un code Nitro est valide ou pas)
```py
    url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}", proxies=proxy_param, timeout=5)
```

- Si la requête réussit/si le code est bon (code de statut HTTP 200), ça va écrire le code Nitro dans un fichier texte appelé "nitrovalidcodes" et vous prévenir par un print
```py
    if url.status_code == 200:
        with open("nitrovalidcodes.txt", "w") as nitrovalidfile:
            nitrovalidfile.write(nitro)
        print(f"Code Nitro valide : {nitro}")
```

- Sinon, on affiche un message d'erreur
```py
    else:
        print("Code Nitro non valide")
```

---

### FAQ :

- Q : Pourquoi j'ai besoin de proxies ?
- A : Pour faire simple, imaginez-vous que 1 proxy est égal à une connexion Internet (ce qui n'est pas le cas). Et bien l'API de Discord n'autorise que un certain nombre d'utilisation par jour de leur API par proxy. C'est-à-dire que votre connexion Internet n'aura le droit que à un certain nombre d'utilisation après, il faudra attendre 24h pour pouvoir le ré-utiliser. Et bien l'utilité d'utiliser plusieurs connexion Internet (proxy) est de pouvoir bypass (passer) cette limitation en simulant que ce n'est pas notre connexion Internet (comme si on utilisait un VPN).

- Q : Pourquoi je n'ai jamais de Nitro valide ?
- A : Car les chances d'avoir généré un Nitro valide sont extrèmement petite !

- Q : Mais du coup, le code ne fonctionne pas ?
- A : Le code est bel et bien fonctionnel, si vous générez un Nitro valide et que vous le checkez, il sera détecté comme valide mais comme je l'ai dit, les chances sont extrèmement petite de tomber sur un Nitro bel et bien valide.

- Q : Il y a-t-il un virus/token grab ?
- A : Vous avez juste à lire l'explication du code entier pour comprendre que le code ne présente aucun virus/token grab et que le code est bel et bien safe.
