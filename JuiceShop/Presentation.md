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

## Étape 1 : Connexion au compte administrateur

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

## Étape 2 : Connexion au compte de Bender

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

## Pourquoi cette étape est cruciale ?

Les attaques par injection SQL sont parmi les vulnérabilités les plus courantes et les plus dangereuses dans les applications web. Les participants apprendront ainsi à identifier ces vulnérabilités et à comprendre les conséquences des failles d'authentification.

## Résumé des étapes

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

# Quatrième étape de l'investigation : Accéder à des informations sensibles (Sensitive Data Exposure)

## Objectif

L'objectif de cette étape est d'illustrer la notion d'**exposition de données sensibles** (Sensitive Data Exposure) en essayant d'accéder à des informations que vous ne devriez pas voir en tant qu'utilisateur ordinaire. Cela peut inclure des données confidentielles comme des informations personnelles, des mots de passe, des clés d'API, des données bancaires ou des fichiers sensibles qui sont mal protégés sur le site. Cette étape met en évidence l'importance de sécuriser les données sensibles pour éviter qu'elles ne soient exposées à des utilisateurs non autorisés.

## Étape 1 : Exploration des pages et des répertoires

1. **Explorer les URL et les paramètres de l'application** :
   - Commencez par explorer l'application web comme un utilisateur normal. Allez sur les pages accessibles sans authentification et examinez les URL.
   - Recherchez des paramètres sensibles dans l'URL, tels que des identifiants utilisateur, des tokens, ou d'autres informations qui pourraient vous permettre d'accéder à des données sensibles si elles sont mal protégées.

2. **Manipulation des URL et accès à des zones non protégées** :
   - Tentez de manipuler les URL en modifiant certains paramètres ou en accédant à des ressources protégées par des règles d'accès non strictes.
   - Essayez de deviner des chemins ou des fichiers qui pourraient contenir des informations sensibles, comme `/admin/config`, `/user/data`, ou `/backup`, ou `/ftp`.

## Étape 2 : Inspection des réponses du serveur

1. **Analyser les réponses du serveur** :
   - Observez attentivement les réponses du serveur lors de vos tentatives d'accès. Si le serveur renvoie des informations qui ne sont pas normalement accessibles, cela peut indiquer une vulnérabilité d'exposition de données sensibles.
   - Par exemple, vous pourriez obtenir des détails sur des utilisateurs, des fichiers de configuration contenant des mots de passe en texte clair, ou des données sensibles comme des numéros de carte de crédit ou des informations bancaires.

2. **Rechercher des fichiers de configuration mal sécurisés** :
   - Vérifiez si des fichiers de configuration importants (par exemple, des fichiers de configuration du serveur, des clés API ou des bases de données) sont accessibles sans restrictions appropriées.
   - Par exemple, si des fichiers comme `config.php`, `.env` ou `backup.tar.gz` sont présents dans les répertoires publics ou accessibles via l'URL, cela peut constituer une grave exposition de données sensibles.

## Étape 3 : Accès aux données sensibles (exemple avec un fichier de sauvegarde)

1. **Explorer les répertoires accessibles** :
   - Si l'application met à disposition des répertoires de sauvegarde ou des répertoires non protégés par une authentification stricte, explorez-les à la recherche de fichiers sensibles.
   - Par exemple, si un fichier de sauvegarde (comme `backup.zip` ou `database.sql`) est accessible, vous pourriez y trouver des informations sensibles telles que des identifiants, des mots de passe, des données personnelles, etc.

2. **Téléchargement de fichiers sensibles** :
   - Si vous trouvez un fichier qui semble contenir des données sensibles, téléchargez-le (si possible) et examinez-le pour vérifier qu'il contient des informations confidentielles qui ne devraient pas être accessibles à un utilisateur non autorisé.
   - Vérifiez le contenu de ces fichiers pour identifier des données sensibles comme des mots de passe non cryptés, des informations personnelles des utilisateurs, ou d'autres secrets.

## Étape 4 : Identification de la vulnérabilité d'exposition de données sensibles

1. **Exposition de données sensibles dans les réponses HTTP** :
   - Parfois, des informations sensibles peuvent être renvoyées directement dans les réponses HTTP, par exemple dans des cookies, des en-têtes HTTP ou des pages d'erreur. 
   - Si vous trouvez des informations sensibles dans ces réponses, cela démontre que les données ne sont pas correctement protégées et sont exposées de manière involontaire.

2. **Réflexion sur la sécurité des données sensibles** :
   - L'objectif de cette étape est de démontrer comment des données sensibles peuvent être exposées à des utilisateurs non autorisés, souvent à cause de mauvaises configurations ou de mauvaises pratiques de sécurité.
   - Une fois que vous avez trouvé des données sensibles, il est important de réfléchir à la manière dont elles devraient être protégées, par exemple en utilisant le cryptage des données sensibles, en mettant en place des contrôles d'accès stricts, ou en validant correctement les permissions d'accès à certains fichiers.

### Pourquoi cette étape est importante ?

L'exposition de données sensibles est une vulnérabilité critique qui peut entraîner des conséquences graves, telles que le vol d'identité, la fraude financière, ou la compromission de systèmes sensibles. Les entreprises doivent être conscientes des risques associés à l'exposition non intentionnelle de données sensibles et mettre en œuvre des mécanismes de sécurité solides pour protéger ces informations.

Les bonnes pratiques pour éviter l'exposition de données sensibles incluent :
- **Cryptage des données sensibles** en transit (SSL/TLS) et au repos (base de données cryptées).
- **Contrôles d'accès stricts** pour limiter les utilisateurs autorisés à accéder à des données sensibles.
- **Mise en œuvre de l'authentification forte** pour les utilisateurs qui accèdent à des informations sensibles.
- **Validation des permissions** et sécurisation des répertoires et fichiers sensibles pour empêcher leur accès non autorisé.

## Résumé des étapes

- **Objectif** : Identifier et accéder à des données sensibles qui ne devraient pas être visibles pour un utilisateur ordinaire.
- **Méthode** :
  - Exploration des URL et manipulation des paramètres pour accéder à des répertoires ou fichiers sensibles.
  - Inspection des réponses du serveur pour détecter la présence d'informations sensibles.
  - Téléchargement de fichiers sensibles ou accès à des fichiers mal sécurisés (par exemple, sauvegardes, fichiers de configuration).
  - Analyse des risques d'exposition de données sensibles et réflexion sur les mesures de sécurité nécessaires.

# Cinquième étape de l'investigation : Contourner les restrictions de téléchargement avec Poison Null Byte

## Objectif

Dans cette étape, nous allons tenter de contourner la restriction qui empêche le téléchargement de certains fichiers, en utilisant une technique appelée **Poison Null Byte**. Cette méthode nous permet de manipuler l'URL pour contourner la restriction de type de fichier et accéder à des informations sensibles qui étaient autrement bloquées.

## Étape 1 : Analyser le problème de téléchargement

Lorsque vous tentez de télécharger le fichier **`package.json.bak`** situé dans le répertoire **`/ftp/`**, vous obtenez une erreur **403 - Forbidden**, ce qui signifie que le serveur interdit l'accès à ce fichier. Le message d'erreur indique également que seuls les fichiers avec les extensions **.md** et **.pdf** sont autorisés au téléchargement.

## Étape 2 : Comprendre la technique du Poison Null Byte

Le **Poison Null Byte** est un exploit basé sur un caractère spécial appelé **byte nul** (noté **`%00`** dans les URL). Ce caractère est un **terminateur de chaîne** dans de nombreux systèmes et langages de programmation. Cela signifie que lorsqu'un byte nul est rencontré, le système considère que la chaîne de caractères (comme un nom de fichier ou une URL) se termine à cet endroit.

En insérant un Poison Null Byte dans le nom du fichier que nous tentons de télécharger, nous pouvons tromper le serveur. Le Poison Null Byte va forcer le serveur à **ignorer la partie de l'extension du fichier après ce caractère**. Par exemple, en ajoutant un Poison Null Byte après **`package.json`**, le serveur pourrait ne voir que **`package.json`**, mais avec une extension autorisée comme **`.md`**.

## Étape 3 : Appliquer l'encodage URL au Poison Null Byte

Dans une URL, un Poison Null Byte (qui est normalement écrit **`%00`**) doit être encodé pour être correctement transmis. Le Poison Null Byte encodé en URL est **`%2500`**.

## Étape 4 : Manipuler l'URL pour contourner la restriction

Pour contourner la restriction de téléchargement des fichiers, modifions l'URL de la manière suivante :

1. L'URL initiale pour télécharger le fichier **`package.json.bak`** serait quelque chose comme :

    ```
    http://10.10.90.39/ftp/package.json.bak
    ```

2. Pour contourner la restriction des extensions, nous allons ajouter le Poison Null Byte encodé en URL **`%2500`** à la fin du nom du fichier, puis ajouter une extension **`.md`** à la fin. Cela donnera :

    ```
    http://10.10.90.39/ftp/package.json.bak%2500.md
    ```

## Étape 5 : Télécharger le fichier

En accédant à l'URL modifiée, le serveur va traiter le nom du fichier comme **`package.json.md`** au lieu de **`package.json.bak`**, car le Poison Null Byte force le serveur à ignorer la partie après le byte nul. Le fichier sera alors téléchargé avec l'extension **`.md`**, qui est autorisée, même si l'extension réelle du fichier est **`.bak`**.

## Pourquoi cette méthode fonctionne-elle ?

Cette méthode fonctionne grâce au comportement des **terminateurs de chaîne** dans de nombreux systèmes de fichiers et langages de programmation. Le byte nul **`%00`** est utilisé pour signaler la fin de la chaîne de caractères, ce qui permet de tronquer l'URL à ce point précis. En encodant ce byte nul en **`%2500`** (l'encodage URL du byte nul), nous pouvons manipuler l'URL de manière à faire en sorte que le serveur ignore la partie du nom de fichier après le Poison Null Byte, contournant ainsi les restrictions de téléchargement.

## Conclusion

Le Poison Null Byte est une technique puissante pour contourner les restrictions sur les types de fichiers téléchargés. Dans cette étape, vous avez vu comment cette technique permet de tromper le serveur et de télécharger un fichier normalement interdit, en exploitant une faiblesse dans la manière dont les systèmes traitent les chaînes de caractères et les extensions de fichiers.

Cela illustre l'importance de vérifier et de sécuriser correctement les mécanismes de validation des fichiers et des entrées utilisateurs afin d'éviter des vulnérabilités telles que l'**exploitation de données sensibles**.

