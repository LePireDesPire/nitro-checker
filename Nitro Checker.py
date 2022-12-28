import requests

with open("nitros.txt", "r") as nitrofile:
    nitros =nitrofile.read().split("\n")
nitrofile.close()
#En gros, ce qui est au dessus c'est pour ouvrir le fichier texte qui est rempli de code Nitro que vous voulez check.

with open ("proxies.txt", "r") as proxiefile:
    proxies = proxiefile.read().split("\n")
proxiefile.close()
#En gros, ce qui est au dessus c'est pour ouvrir le fichier texte qui contient vos proxies. (Il vous faut impérativement le même nombre/plus de proxies que de Nitro car si vous le faites sans proxies (c'est à dire, avec votre "connexion" en quelques sortes), ça ne va plus rien check car à partir d'un moment, le proxy n'a plus le droit/ne peut plus pendant 24h il me semble de check la validité d'un nitro via l'API)

for i in range(len(nitros)):
    nitro = nitros[1]
    proxy = proxies[1]
#En gros, ce qui est au dessus c'est pour dire que chaque nitro que vous allez check sera check par un proxy 
    ProxyParam = {"http://": proxy, "https://": proxy}
    url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}", proxies=ProxyParam, timeout=5)

    if url.status_code == 200:
        with open("nitrovalidcodes.txt", "w") as nitrovalidfile:
            nitrovalidfile.write(nitro)
        nitrovalidfile.close()
        print(f"Valid code : {nitro}")
    else:
        print("Nitro not valid")
#En gros, ce qui est au dessus c'est pour check via l'API de Discord si le Nitro est valide ou pas. Si il est valide, ça va vous dire "Valid code : le code nitro" et ça va directement stocker le code dans un fichier texte nommé "nitrovalidcodes". Sinon, il y aura juste écrit "Nitro not valid".
#ATTENTION : Le code fonctionne bel et bien mais les chances d'avoir un nitro valide est de je ne sais pas combien (= beaucoup).

#By LePireDesPire#9904 :)
