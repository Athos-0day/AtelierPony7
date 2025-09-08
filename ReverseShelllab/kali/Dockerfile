# Utilise l'image officielle Kali Linux
FROM kalilinux/kali-rolling

# Évite les prompts interactifs (ex: tzdata)
ENV DEBIAN_FRONTEND=noninteractive

# Mise à jour + installation des outils utiles
RUN apt-get update && \
    apt-get install -y \
        netcat \
        curl \
        nmap \
        metasploit-framework \
        gnupg \
        lsb-release && \
    apt-get clean

# Ouvre directement un shell interactif à l'exécution
CMD ["/bin/bash"]
