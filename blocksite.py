import os

site = input("Digite o nome do site que deseja bloquear (ex: google.com): ")

with open(r"C:\Windows\System32\drivers\etc\hosts", "a") as file:
	file.write("\n127.0.0.1               {}\n".format(site))

# limpa o cache DNS, garantindo que as alterações sejam aplicadas imediatamente
os.system("ipconfig /flushdns")