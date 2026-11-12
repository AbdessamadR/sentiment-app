# Fiche de cadrage : Questions sur le règlement intérieur

## Besoin en une phrase (obligatoire)

Développer un assistant intelligent permettant aux étudiants d'obtenir des réponses fiables à leurs questions sur le règlement intérieur de l'école, en s'appuyant sur les documents officiels.

## Utilisateur final (obligatoire)

Les étudiants de l'école qui souhaitent comprendre les règles, les procédures et les obligations liées à leur scolarité.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille)

Le RAG est adapté car (b) les réponses doivent être vérifiables à partir des articles du règlement intérieur, avec des références aux passages utilisés. De plus, (d) une réponse incorrecte peut induire les étudiants en erreur concernant leurs droits et leurs obligations ; il est donc important de limiter les réponses aux informations présentes dans les documents officiels.

## Données nécessaires et leur origine (obligatoire)

Les données nécessaires sont les documents officiels du règlement intérieur, les procédures administratives et les éventuelles notes de service publiées par l'établissement. Ces documents seront fournis par l'administration de l'école et devront être régulièrement mis à jour.

## Métrique de succès et seuil d'acceptation (obligatoire)

Utiliser un jeu de questions-réponses validées par l'administration pour mesurer le taux de réponses correctes et correctement justifiées par les documents. Le seuil d'acceptation proposé est d'au moins 90 % de réponses correctes avec une référence pertinente.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une réponse incorrecte peut entraîner une mauvaise compréhension des règles ou des procédures scolaires par un étudiant. L'assistant devra signaler lorsqu'il ne trouve pas d'information suffisante et orienter l'étudiant vers l'administration pour les questions sensibles ou non couvertes par les documents.

## Risques éthiques ou de confidentialité (obligatoire)

Les documents internes peuvent contenir des informations confidentielles ou des données personnelles. L'accès aux documents devra être contrôlé et les données personnelles non nécessaires devront être exclues de l'indexation.

## Approche écartée et pourquoi (facultatif)

Un modèle génératif seul est écarté, car il peut produire des informations non présentes dans le règlement intérieur. Le RAG permet de fonder les réponses sur les documents officiels et de fournir des références vérifiables.