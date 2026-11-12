# sentiment-app : dépôt du binôme

Application fil rouge du cours **Développement et déploiement d'applications intelligentes**.

Ce dépôt grandit chaque semaine. La semaine 1 met en place le cadrage du projet, l'environnement de développement et les premiers tests automatisés.

## Installation

### 1. Cloner le dépôt

```bash
git clone <URL_DU_DEPOT>
cd sentiment-app
```

### 2. Créer l'environnement virtuel

```bash
python -m venv .venv
```

### 3. Activer l'environnement virtuel

**Avec CMD (Windows) :**

```cmd
.venv\Scripts\activate.bat
```

**Avec PowerShell (Windows) :**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Avec Linux / macOS :**

```bash
source .venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

## Vérifier son installation

Vérifier que l'environnement est correctement configuré :

```bash
python scripts/check_setup.py
```

Lancer les tests automatisés :

```bash
pytest -q
```

La démarche complète de test, étape par étape, est disponible dans le fichier `TESTS.md`.

## Structure du projet

```text
sentiment-app/
│
├── app/                    # Code source de l'application
│
├── data/                   # Données du projet
│   └── sample_reviews.csv  # Jeu de données d'exemple
│
├── docs/
│   └── cadrage/             # Fiches de cadrage des cas d'usage
│       ├── BANQUE-DE-CAS.md
│       ├── cas1-pharmacie.md
│       ├── cas2-reglement.md
│       ├── cas3-avis-negatifs.md
│       ├── EXEMPLE-corrige.md
│       └── TEMPLATE.md
│
├── models/                  # Modèles entraînés
│
├── scripts/                 # Scripts utilitaires
│   └── check_setup.py
│
├── tests/                   # Tests automatisés
│
├── .env.example             # Exemple de configuration
├── .gitignore               # Fichiers exclus de Git
├── requirements.txt         # Dépendances Python
├── TESTS.md                 # Guide d'exécution des tests
└── README.md                # Documentation principale
```

## Cas d'utilisation étudiés

Trois cas d'utilisation ont été étudiés pendant la première semaine :

| Cas | Approche envisagée | Objectif |
|---|---|---|
| Gestion des ordonnances en pharmacie | Règles métier | Vérifier les ordonnances et détecter les informations manquantes |
| Questions sur le règlement scolaire | RAG | Répondre aux questions en s'appuyant sur les documents de référence |
| Analyse des avis négatifs | Machine Learning | Classifier et prioriser les avis clients négatifs |

Les objectifs et critères d'acceptation sont détaillés dans `docs/cadrage/`.

## Configuration

Un fichier `.env.example` est fourni comme modèle de configuration.

Pour créer votre propre fichier de configuration :

```bash
copy .env.example .env
```

Sous Linux / macOS :

```bash
cp .env.example .env
```

Le fichier `.env` contient les paramètres locaux et ne doit pas être envoyé sur Git.

## Tests

Pour exécuter tous les tests :

```bash
pytest -q
```

Pour exécuter uniquement les tests de cadrage :

```bash
pytest tests/test_cadrage.py -q
```

Pour vérifier la configuration de l'environnement :

```bash
python scripts/check_setup.py
```

## Gestion du projet avec Git

Chaque membre du binôme doit effectuer des contributions réelles et les enregistrer avec sa propre identité Git.

Vérifier les contributions :

```bash
git shortlog -sn --all
```

Consulter l'historique des commits :

```bash
git log --oneline
```

## Membres du binôme

| Rôle | Nom | Identifiant GitHub | Travail de la semaine 1 |
|---|---|---|---|
| Membre A | [Nom du membre A] | [@login] | Initialisation du projet et cadrage |
| Membre B | [Nom du membre B] | [@login] | Documentation et installation sous Windows |

---

**Projet pédagogique — Développement et déploiement d'applications intelligentes.**