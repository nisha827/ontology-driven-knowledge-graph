from odkg.metrics import pairwise_precision_recall


def test_pairwise_precision_recall():
    result = pairwise_precision_recall([("a", "b"), ("a", "c")], [("a", "b"), ("b", "c")])
    assert result["precision"] == 0.5
    assert result["recall"] == 0.5
    assert result["f1"] == 0.5


def test_empty_predictions_are_zero():
    result = pairwise_precision_recall([], [("a", "b")])
    assert result["precision"] == result["recall"] == result["f1"] == 0.0
