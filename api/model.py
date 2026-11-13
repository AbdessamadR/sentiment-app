"""Raccord entre l'API et le modèle entraîné au TP2."""

from typing import Literal, TypedDict

from sentiment_app.predict import charger_modele
from sentiment_app.predict import predict as _predict

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