# Fiche de cadrage : Ordonnances incomplètes en pharmacie

## Besoin en une phrase (obligatoire)

Détecter automatiquement les informations obligatoires manquantes dans les ordonnances afin d'aider les pharmaciens à vérifier leur complétude avant leur traitement.

## Utilisateur final (obligatoire)

Les pharmaciens et les préparateurs en pharmacie, qui utilisent l'application comme outil d'aide à la vérification des ordonnances.

## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(b) Les champs obligatoires peuvent être contrôlés à l'aide de règles explicites et vérifiables. (d) Une ordonnance déclarée complète à tort peut présenter un risque pour la sécurité du patient, ce qui impose une validation humaine.

## Données nécessaires et leur origine (obligatoire)

Des ordonnances numérisées ou structurées contenant les informations nécessaires à leur vérification, ainsi que les exigences réglementaires applicables et les règles propres à chaque type d'ordonnance. Les données de santé doivent être protégées et leur accès limité aux personnes autorisées.

## Métrique de succès et seuil d'acceptation (obligatoire)

Mesurer le rappel de détection des ordonnances incomplètes sur un jeu de test validé par des professionnels de santé, avec un objectif d'au moins 98 %. Les faux négatifs seront particulièrement surveillés afin de limiter les ordonnances incomplètes déclarées complètes.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une ordonnance incomplète déclarée complète à tort peut entraîner un risque pour la sécurité du patient. Le pharmacien doit examiner les alertes et confirmer la conformité avant toute décision de traitement.

## Risques éthiques ou de confidentialité (obligatoire)

Les ordonnances contiennent des données personnelles et de santé sensibles. Leur traitement nécessite un stockage sécurisé, une limitation des accès, une minimisation des données et le respect de la réglementation applicable.

## Approche écartée et pourquoi (facultatif)

Le Machine Learning n'est pas prioritaire, car les contrôles principaux reposent sur des règles explicites et vérifiables. Il pourrait toutefois compléter le système pour extraire les informations depuis des ordonnances manuscrites.