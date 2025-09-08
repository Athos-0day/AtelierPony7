FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

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
    passwd

### 1. Création des utilisateurs

# Utilisateur vulnérable
RUN useradd -m user && echo "user:password" | chpasswd && adduser user sudo

# Utilisateur de départ
RUN useradd -m ctfplayer && echo "ctfplayer:ctfpass" | chpasswd

### 2. Configurations de failles

# Fichier SUID vulnérable (dans le home de user)
COPY suid_privesc.c /home/user/suid_privesc.c
RUN gcc /home/user/suid_privesc.c -o /home/user/suid_bin && \
    chmod 4755 /home/user/suid_bin && \
    chown root:root /home/user/suid_bin && \
    rm /home/user/suid_privesc.c

# Ajouter une mauvaise config sudo pour `user`
RUN echo "user ALL=(ALL) NOPASSWD: /usr/bin/vim" >> /etc/sudoers

### 3. Ajout des flags

# Flag pour user uniquement
RUN echo "FLAG-USER{user-level-access-achieved}" > /home/user/user.txt && \
    chown user:user /home/user/user.txt && \
    chmod 640 /home/user/user.txt

# Flag root
RUN echo "FLAG-ROOT{root-access-obtained}" > /root/root.txt && \
    chmod 600 /root/root.txt

### 4. Connexion automatique en tant que `ctfplayer`

# Set l’utilisateur par défaut
USER ctfplayer
WORKDIR /home/ctfplayer

CMD ["/bin/bash"]
