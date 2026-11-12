
"""Raccord entre l'API et le modèle entraîné au TP2."""

import sys
from pathlib import Path
from typing import Literal, TypedDict

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))

from predict import charger_modele, predict as _predict  # noqa: E402

SEUIL_ABSTENTION = 0.70

SentimentLabel = Literal["POSITIVE", "NEGATIVE", "INDETERMINE"]


class PredictionResult(TypedDict):
    """Contrat de sortie d'une prédiction."""

    label: SentimentLabel
    score: float
    text: str


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec mécanisme d'abstention."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        charger_modele()

    def predict(self, text: str) -> PredictionResult:
        """Renvoie POSITIVE, NEGATIVE ou INDETERMINE."""
        resultat = _predict(text)

        label: SentimentLabel = resultat["label"].upper()
        score = resultat["score"]

        if score < SEUIL_ABSTENTION:
            label = "INDETERMINE"

        return {
            "label": label,
            "score": score,
            "text": text[:100],
        }


def load_model() -> SentimentClassifier:
    """Construit le classifier."""
    return SentimentClassifier()
