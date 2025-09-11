# Utilisation d'une image officielle PHP avec Apache
FROM php:7.4-apache

# Activation de mod_rewrite et autres modules utiles
RUN docker-php-ext-install mysqli && a2enmod rewrite

# Création du répertoire d'upload (volontairement world-writable)
RUN mkdir /var/www/html/upload && chmod 777 /var/www/html/upload

# Ajout du fichier vulnérable upload.php
COPY upload.php /var/www/html/upload.php
RUN chmod 777 /var/www/html/upload.php

# Ajout d’un flag caché dans le système
RUN echo "FLAG{Bravo_tu_as_obtenu_un_reverse_shell}" > /flag.txt

# Exposition du port web
EXPOSE 80

# Lancement d'Apache au premier plan
CMD ["apache2-foreground"]
