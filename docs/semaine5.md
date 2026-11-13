# Semaine 5 : l'interface, notes du binôme

> Trois questions, quelques phrases chacune. Répondez avec ce que vous avez observé.

## 1. Pourquoi l'interface n'importe-t-elle jamais `predict()` ni le fichier `.joblib` ?

L'interface Streamlit ne charge pas directement le modèle et n'importe pas la fonction `predict()`. Elle communique avec l'API FastAPI à travers le client HTTP défini dans `ui/client.py`. C'est l'API qui utilise le modèle `.joblib` pour effectuer les prédictions. Cette séparation permet de distinguer l'interface utilisateur de la logique métier et du modèle, et facilite la maintenance et l'évolution de l'application.

## 2. Que montre l'interface quand le modèle hésite, et pourquoi est-ce mieux qu'un verdict forcé ?

Lorsque le modèle n'est pas suffisamment sûr de sa prédiction, l'interface affiche : « Je ne sais pas : à faire vérifier par un humain ». Par exemple, avec le texte inventé `xqzvb wlkptr grombu`, le modèle a affiché une confiance de 52 % et s'est abstenu de donner un verdict. Cette approche est préférable à une décision forcée, car elle évite de présenter une prédiction incertaine comme une réponse fiable et permet une vérification humaine.

## 3. Que voit l'utilisateur quand l'API tombe ? Et le fichier `data/avis_exemple.csv` : combien d'avis partent vers un humain ?

Lorsque l'API est indisponible, le client est prévu pour afficher un message indiquant que l'API est injoignable et qu'il faut lancer le serveur FastAPI. Ce comportement est prévu dans le code, mais nous n'avons pas réalisé le test de déconnexion de l'API.

Avec le fichier `data/avis_exemple.csv`, l'interface a traité 6 avis : 2 positifs, 2 négatifs et 2 indéterminés. Ainsi, 2 avis sur 6, soit environ 33 %, sont orientés vers une vérification humaine.