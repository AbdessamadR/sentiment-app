
"""Tests d'intégration de l'API (TP4, étape D)."""

from pathlib import Path

import pytest

MODELE = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"

pytestmark = pytest.mark.skipif(
    not MODELE.exists(),
    reason="modèle non produit : python src/train.py",
)


def test_demarrage_reel_charge_le_modele():
    """D.1 : le démarrage charge réellement le modèle."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        reponse = client.get("/health")

    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]



def test_modele_absent_refuse_le_demarrage(monkeypatch):
    """D.2 : l'API refuse de démarrer si le modèle est absent."""
    from fastapi.testclient import TestClient

    import api.model as module_model
    from api.main import app

    def chargement_impossible():
        raise FileNotFoundError("Modèle absent")

    monkeypatch.setattr(
        module_model,
        "charger_modele",
        chargement_impossible,
    )

    with pytest.raises(FileNotFoundError, match="Modèle absent"):
        with TestClient(app):
            pass


def test_modele_non_charge_renvoie_503(monkeypatch):
    """D.3 : les routes protégées renvoient 503 sans modèle."""
    from fastapi.testclient import TestClient

    from api.main import app

    with TestClient(app) as client:
        monkeypatch.delattr(app.state, "classifier", raising=False)

        reponse_health = client.get("/health")
        reponse_predict = client.post(
            "/predict",
            json={"text": "Livraison rapide et excellente"},
        )

    assert reponse_health.status_code == 503
    assert reponse_predict.status_code == 503


@pytest.mark.parametrize(
    "erreur",
    [
        RuntimeError("panne du modèle"),
        ValueError("bug interne"),
    ],
)
def test_erreur_prediction_renvoie_500_sans_detail(monkeypatch, erreur):
    """D.4 : les erreurs internes ne sont jamais exposées au client."""
    from fastapi.testclient import TestClient

    from api.main import app

    class FauxClassifier:
        model_name = "modele-test"

        def predict(self, text):
            raise erreur

    with TestClient(app) as client:
        monkeypatch.setattr(
            app.state,
            "classifier",
            FauxClassifier(),
        )

        reponse = client.post(
            "/predict",
            json={"text": "Un avis de test"},
        )

    assert reponse.status_code == 500
    assert reponse.json()["detail"] == "Erreur interne du serveur"
    assert str(erreur) not in reponse.text
