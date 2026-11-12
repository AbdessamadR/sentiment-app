# Fiche de cadrage : Priorisation des avis négatifs

## Besoin en une phrase (obligatoire)

Développer un système intelligent permettant d'analyser les avis clients d'un site e-commerce et de prioriser automatiquement les avis négatifs nécessitant une intervention rapide du service client.

## Utilisateur final (obligatoire)

Les responsables du service client et les équipes chargées de la gestion des réclamations, qui souhaitent identifier rapidement les avis nécessitant une attention particulière.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille)

Le Machine Learning est adapté car (a) un jeu de données d'avis clients annotés peut être constitué afin d'entraîner et d'évaluer un modèle de classification. De plus, (c) le volume important d'avis nécessite une solution automatisée avec un coût de traitement par requête relativement faible. Le modèle pourra classer les avis selon leur niveau de priorité.

## Données nécessaires et leur origine (obligatoire)

Les données nécessaires sont les avis publiés par les clients, leur contenu textuel, les notes attribuées et les historiques de traitement des réclamations. Ces données proviendront de la plateforme e-commerce et devront être annotées par des personnes compétentes si les catégories de priorité ne sont pas déjà disponibles.

## Métrique de succès et seuil d'acceptation (obligatoire)

Utiliser le rappel (Recall) de la classe des avis prioritaires pour mesurer la capacité du modèle à identifier les avis nécessitant une intervention. Le seuil d'acceptation proposé est un rappel d'au moins 90 % sur un jeu de test indépendant.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un avis urgent classé comme non prioritaire peut retarder le traitement d'une réclamation et détériorer la satisfaction du client. Les avis classés comme prioritaires seront examinés et validés par un membre du service client avant toute décision.

## Risques éthiques ou de confidentialité (obligatoire)

Les avis peuvent contenir des données personnelles, des coordonnées ou des informations sensibles sur les clients. Il faudra anonymiser les informations inutiles, limiter l'accès aux données et éviter les biais liés au vocabulaire ou au style d'expression des clients.

## Approche écartée et pourquoi (facultatif)

Les règles métier seules sont écartées car elles risquent de ne pas reconnaître les différentes formulations et nuances exprimées dans les avis. Le RAG n'est pas nécessaire ici, car l'objectif principal est de classer et de prioriser les avis plutôt que de répondre à des questions à partir de documents.