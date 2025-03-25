# Juice Shop

## Introduction

Le **Juice Shop** est une application web vulnérable conçue pour aider à la sensibilisation à la sécurité informatique et à l'apprentissage des techniques de piratage éthique. Développée par le projet **OWASP** (Open Web Application Security Project), le Juice Shop simule une application de commerce en ligne vendant des jus de fruits. Cependant, contrairement aux applications de commerce électronique classiques, cette application est intentionnellement conçue avec de nombreuses failles de sécurité, qui permettent aux utilisateurs de tester et d'explorer les différentes vulnérabilités courantes que l'on peut rencontrer dans le développement web.

Les failles que l'on peut trouver dans Juice Shop incluent des attaques telles que l'injection SQL, la manipulation de sessions, l'élévation de privilèges, et bien d'autres. Cela en fait une ressource précieuse pour les développeurs, les testeurs de sécurité et les professionnels de l'informatique souhaitant renforcer leurs compétences en matière de sécurité des applications.

L'objectif de Juice Shop est de fournir un environnement pratique pour découvrir et résoudre ces vulnérabilités dans un cadre contrôlé, tout en apprenant des techniques utilisées par les attaquants dans un but pédagogique.

---

## Outils utiles

Pour tester et exploiter les vulnérabilités de l'application Juice Shop, il est fortement conseillé d'utiliser **Burp Suite**, un outil populaire pour l'analyse de la sécurité des applications web. Burp Suite permet d'intercepter, d'analyser et de manipuler le trafic HTTP/HTTPS entre votre navigateur et le serveur, ce qui est extrêmement utile pour détecter les failles de sécurité.

### Configuration de Burp Suite

Une fois Burp Suite installé, vous devez configurer votre navigateur pour que tout le trafic passe par l'intercepteur de Burp Suite. Vous avez deux options :

1. **Configurer FoxyProxy** : FoxyProxy est une extension pour les navigateurs web qui permet de gérer facilement les paramètres de proxy. Vous pouvez configurer FoxyProxy pour diriger le trafic de votre navigateur via Burp Suite.
   
2. **Utiliser le navigateur intégré de Burp Suite** : Burp Suite offre également un navigateur intégré, que vous pouvez utiliser directement pour interagir avec Juice Shop. Cela évite de devoir configurer un proxy manuellement.

### Utilisation sans Burp Suite

Bien que l'utilisation de Burp Suite soit fortement recommandée pour une analyse approfondie des vulnérabilités, il est tout à fait possible d'interagir avec Juice Shop sans cet outil. Vous pouvez utiliser n'importe quel autre navigateur et tester les fonctionnalités de l'application à la main. Cependant, vous perdrez les avantages d'intercepter et de manipuler directement les requêtes HTTP/HTTPS.

---

## Mots de passe

Dans le cadre de l'exploitation des vulnérabilités de Juice Shop, il est souvent nécessaire de tester des mots de passe, en particulier lors des attaques de brute force ou de dictionnaire. Une liste de mots de passe fréquemment utilisée, appelée **best1050.txt**, est mise à disposition dans le répertoire Git du projet.

### Utilisation de la liste de mots de passe

Vous pouvez utiliser cette liste pour tester différentes combinaisons de mots de passe dans le cadre de vos tests de sécurité. Deux outils populaires pour ce type d'attaque sont **Hydra** et **Burp Suite**. Voici comment les utiliser :

1. **Hydra** : Hydra est un outil en ligne de commande permettant de réaliser des attaques par force brute sur différents protocoles. Pour l'utiliser avec la liste `best1050.txt`, il suffit de spécifier l'URL de Juice Shop et le fichier de mots de passe comme paramètre.

2. **Burp Suite** : Si vous préférez une solution graphique, vous pouvez également utiliser Burp Suite pour effectuer une attaque par brute force. En utilisant la fonctionnalité de **Repetitions** ou en configurant un **Intruder**, vous pouvez tester les mots de passe de la liste `best1050.txt` contre l'application Juice Shop.

### Conclusion

Quel que soit l'outil que vous choisissez, l'utilisation de cette liste de mots de passe vous aidera à mieux comprendre et tester les vulnérabilités liées à l'authentification et à la gestion des mots de passe dans l'application. Vous pouvez choisir l'outil qui vous semble le plus adapté en fonction de vos préférences et de votre niveau d'expérience.

---

