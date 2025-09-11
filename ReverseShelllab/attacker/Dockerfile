FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Installation des outils nécessaires pour l'attaquant
RUN apt-get update && apt-get install -y \
    sudo \
    gcc \
    make \
    vim \
    curl \
    wget \
    net-tools \
    python3 \
    python3-pip \
    git \
    passwd \
    netcat \
    telnet

# Installation des librairies Python nécessaires (ex: requests)
RUN pip3 install requests

# Ajout des fichiers d’exploit dans la VM attaquante
WORKDIR /root
COPY post.py /root/post.py
COPY shell.php /root/shell.php

# Lancement d’un shell interactif par défaut
CMD ["/bin/bash"]
