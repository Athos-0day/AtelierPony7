# Première étape de l'investigation : Exploration du site

La première phase de l'investigation consiste à parcourir le site web et à interagir avec lui de manière manuelle. À ce stade, il n'est pas nécessaire d'activer des outils comme BurpSuite ou d'autres outils d'interception de trafic. En naviguant directement sur l'application, vous pouvez déjà recueillir des informations importantes.

## Ce que vous pouvez chercher :

- **Identification des points d'entrée** : Explorez les différentes pages du site pour identifier les formulaires de saisie, les champs de recherche, les interfaces de connexion, etc.
- **Recherche d'informations sensibles** : Pendant votre navigation, soyez attentif aux informations qui peuvent sembler sensibles ou exposées. Par exemple, il est courant que certaines applications laissent des informations telles que des adresses email dans les messages d'erreur ou dans le code source de la page.
- **Analyse du code source** : Inspectez le code source HTML des pages pour détecter des commentaires, des variables JavaScript ou des liens qui pourraient révéler des informations sensibles ou des points d'entrée pour des attaques.
- **Découverte de l'adresse mail de l'administrateur** : Une première découverte courante pourrait être l'adresse email de l'administrateur, qui peut apparaître dans le code source, dans les pages de contact, ou dans les réponses d'erreur. Cette information pourrait être utile pour de futures étapes de l'investigation.

## Pourquoi cette étape est importante ?

Bien que cette exploration initiale semble basique, elle permet de collecter des informations essentielles sans avoir besoin d'outils spécialisés. L'objectif ici est de mieux comprendre l'architecture du site, de repérer d'éventuelles failles de sécurité évidentes et de recueillir des données qui pourraient être utilisées plus tard dans l'investigation.

Cette phase d'interaction manuelle peut être un premier pas pour repérer des pistes intéressantes avant de passer à des outils plus avancés.

# Deuxième partie de l'investigation : Connexion au compte administrateur et au compte de Bender via manipulation de requêtes SQL

## Objectif

Dans cette étape de l'investigation, l'objectif est de se connecter d'abord au **compte administrateur**, puis au **compte de Bender**, en manipulant les requêtes SQL envoyées au serveur. Vous apprendrez à exploiter des vulnérabilités d'injection SQL pour contourner l'authentification et accéder à des comptes non autorisés. 

Vous pouvez utiliser **Burp Suite** pour intercepter les requêtes et analyser le trafic HTTP, ou manipuler directement les champs du formulaire de connexion pour effectuer l'injection SQL.

### Étape 1 : Connexion au compte administrateur

1. **Accédez à la page de connexion** :
   - Ouvrez le site vulnérable.
   - Identifiez les champs de connexion, notamment le champ pour l'**email** et le **mot de passe**.

2. **Injection SQL pour contourner l'authentification** :
   - Dans le champ **email** ou **mot de passe**, vous allez injecter un payload SQL pour contourner la validation des informations d'identification. Par exemple :
     ```sql
     admin' OR '1'='1
     ```
   - Ce payload modifie la requête SQL envoyée au serveur de manière à ce que la condition `'1'='1` soit toujours vraie, vous permettant ainsi de vous connecter en tant qu'administrateur.

3. **Utilisation de Burp Suite pour intercepter la requête** (optionnel) :
   - Activez **Burp Suite** et configurez-le pour intercepter le trafic HTTP.
   - Soumettez le formulaire de connexion avec le payload injecté. Burp Suite vous permettra de capturer la requête et de l'analyser en détail avant de l'envoyer au serveur.
   - Modifiez la requête si nécessaire pour affiner l'injection SQL et valider votre accès.

### Étape 2 : Connexion au compte de Bender

Après avoir réussi à vous connecter en tant qu'administrateur, la prochaine étape consiste à accéder au **compte de Bender**. 

1. **Accédez à l'interface d'administration ou à la page des utilisateurs** :
   - Il faudra d'abord trouvé l'adresse mail de Bender qui est similaire à celle de l'administrateur d'ailleurs.

2. **Injection SQL pour se connecter au compte de Bender** :
   - Dans le formulaire de connexion pour Bender, vous pouvez à nouveau utiliser une injection SQL pour vous connecter directement en tant que Bender. Par exemple, utilisez un payload comme :
     ```sql
     bender' OR '1'='1
     ```
   - Cela permettra de contourner l'authentification et de vous connecter au compte de Bender, même si vous ne connaissez pas son mot de passe.

3. **Utilisation de Burp Suite pour intercepter et analyser la requête** :
   - Si vous utilisez **Burp Suite**, vous pouvez intercepter et analyser la requête envoyée lors de la tentative de connexion au compte de Bender. Cela vous permettra de voir comment la requête SQL est envoyée et d'adapter votre payload en conséquence.

### Pourquoi cette étape est cruciale ?

Les attaques par injection SQL sont parmi les vulnérabilités les plus courantes et les plus dangereuses dans les applications web. Les participants apprendront ainsi à identifier ces vulnérabilités et à comprendre les conséquences des failles d'authentification.

### Résumé des étapes

- **Objectif** : Se connecter aux comptes administrateur et Bender en exploitant des failles d'injection SQL.
- **Méthode** :
  - Injection SQL dans les champs de saisie du formulaire de connexion.
  - Utilisation de **Burp Suite** pour intercepter et analyser les requêtes HTTP (optionnel).
  - Manipulation des données envoyées au serveur pour contourner les mécanismes d'authentification.

# Troisième étape de l'investigation : Connexion au compte administrateur en utilisant Burp Suite Intruder

## Objectif

Dans cette étape, vous allez utiliser **Burp Suite Intruder** pour effectuer une attaque par force brute sur le formulaire de connexion, en tentant de deviner le mot de passe du compte **administrateur** à partir d'une liste de mots de passe populaires (fichier `best1050.txt`). Cette étape met en évidence les vulnérabilités liées à l'authentification, en particulier l'utilisation de mots de passe faibles pour des comptes avec des privilèges importants.

## Étape 1 : Configuration de Burp Suite pour intercepter la requête

1. **Accédez à la page de connexion** :
   - Comme dans les étapes précédentes, ouvrez le site vulnérable.
   - Localisez le formulaire de connexion où vous entrez votre **email** et **mot de passe**.

2. **Interceptez la requête de connexion** :
   - Activez **Burp Suite** et configurez-le pour intercepter les requêtes HTTP.
   - Soumettez un formulaire avec des informations valides (même si l'email et le mot de passe sont incorrects pour cette étape, l’objectif est simplement de capturer la requête).
   - Burp Suite interceptera la requête POST envoyée au serveur avec les données de connexion.

3. **Envoyez la requête à Intruder** :
   - Une fois la requête interceptée, envoyez-la à l'outil **Intruder** de Burp Suite pour automatiser l'attaque de force brute.
   - Dans l'onglet **Intruder**, identifiez la partie de la requête qui contient le **mot de passe** et sélectionnez cette zone comme **position à attaquer**.

## Étape 2 : Configuration de l'attaque par force brute

1. **Définir la liste des mots de passe** :
   - Téléchargez le fichier de liste de mots de passe `best1050.txt`. Ce fichier contient une série de mots de passe couramment utilisés, classés par fréquence.
   - Dans Burp Suite, configurez Intruder pour utiliser cette liste de mots de passe dans l’attaque de force brute. Cela permettra de tester plusieurs mots de passe populaires pour trouver celui du compte administrateur.

2. **Lancer l'attaque avec Burp Suite Intruder** :
   - Configurez Intruder pour envoyer la requête avec chaque mot de passe de la liste `best1050.txt`.
   - L'attaque par force brute va maintenant tenter d'envoyer différentes combinaisons de mots de passe au serveur pour tenter de se connecter avec un mot de passe valide pour l'administrateur.

## Étape 3 : Analyser les résultats

1. **Observer la réponse du serveur** :
   - Une fois l'attaque lancée, Burp Suite vous montrera les réponses du serveur pour chaque tentative de mot de passe.
   - En fonction de la réponse (par exemple, un message d'erreur différent ou un code de statut HTTP spécifique), vous pourrez identifier quel mot de passe a permis de réussir la connexion. Si un mot de passe valide est trouvé, vous aurez accès au compte administrateur.

2. **Identification du mot de passe vulnérable** :
   - L'attaque de force brute montre l'importance de la complexité des mots de passe. Un mot de passe simple et couramment utilisé (comme un mot de passe de la liste `best1050.txt`) peut facilement être deviné par un attaquant utilisant cette méthode.

## Pourquoi cette étape est importante ?

Cette étape met en lumière les dangers des mots de passe faibles, en particulier pour les comptes avec des privilèges élevés (comme le compte administrateur). Même si l'email et le nom d'utilisateur sont protégés, un mot de passe faible peut facilement permettre à un attaquant d'accéder à des comptes sensibles. Ainsi, il est necessaire d'avoir une politique de mots de passes robustes pour une site web.

## Résumé des étapes

- **Objectif** : Se connecter au compte administrateur en utilisant Burp Suite Intruder et une liste de mots de passe (`best1050.txt`).
- **Méthode** :
  - Interception de la requête de connexion via Burp Suite.
  - Configuration de Burp Suite Intruder pour envoyer des requêtes de force brute avec la liste de mots de passe.
  - Analyse des réponses du serveur pour identifier un mot de passe valide.


