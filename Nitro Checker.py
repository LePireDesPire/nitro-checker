import requests

with open("nitros.txt", "r") as nitrofile:
    nitros = nitrofile.read().split("\n")

with open("proxies.txt", "r") as proxiefile:
    proxies = proxiefile.read().split("\n")

for nitro, proxy in zip(nitros, proxies):
    proxy_param = {"http://": proxy, "https://": proxy}

    url = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}", proxies=proxy_param, timeout=5)
    
    if url.status_code == 200:
        with open("nitrovalidcodes.txt", "w") as nitrovalidfile:
            nitrovalidfile.write(nitro)
        print(f"Code Nitro valide : {nitro}")
    else:
        print("Code Nitro non valide")
