
#!/usr/bin/env python
"""Prédiction unitaire : la fonction que l'API appellera.

Le modèle peut être placé à un emplacement personnalisé grâce à
la variable d'environnement SENTIMENT_MODELE.
"""
import os
import sys
from functools import lru_cache
from pathlib import Path

import joblib

RACINE = Path(__file__).resolve().parents[1]


def chemin_modele() -> Path:
    """Détermine le chemin actuel du modèle."""
    chemin = os.environ.get("SENTIMENT_MODELE")
    if chemin:
        return Path(chemin)
    return RACINE / "models" / "sentiment.joblib"


MODELE = chemin_modele()


@lru_cache(maxsize=1)
def charger_modele():
    """Charge le modèle une seule fois par processus."""
    modele = chemin_modele()
    if not modele.exists():
        raise FileNotFoundError(
            f"Modèle introuvable : {modele}. "
            "Entraînez-le avec python src/train.py "
            "ou définissez SENTIMENT_MODELE."
        )
    return joblib.load(modele)


def predict(texte: str) -> dict:
    """Renvoie {'label': 'positive'|'negative', 'score': float}."""
    if not isinstance(texte, str) or not texte.strip():
        raise ValueError("texte vide")
    pipeline = charger_modele()
    etiquette = pipeline.predict([texte])[0]
    score = float(pipeline.predict_proba([texte]).max())
    return {"label": etiquette, "score": round(score, 4)}


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    resultat = predict(" ".join(sys.argv[1:]))
    print(f"{resultat['label']} (confiance {resultat['score']:.0%})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
