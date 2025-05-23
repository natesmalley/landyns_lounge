from app.classifier import MealClassifier


def test_spaghetti_classification():
    with open("tests/data/spaghetti.ppm", "rb") as f:
        data = f.read()
    clf = MealClassifier()
    assert clf.classify(data) == "pasta"
