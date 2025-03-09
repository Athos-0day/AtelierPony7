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
