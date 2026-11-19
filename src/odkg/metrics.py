"""Small, dependency-light evaluation metrics for labelled entity matches."""
from __future__ import annotations
from collections.abc import Iterable


def pairwise_precision_recall(predicted_pairs: Iterable[tuple[str, str]],
                              gold_pairs: Iterable[tuple[str, str]]) -> dict[str, float]:
    predicted = {tuple(sorted(pair)) for pair in predicted_pairs}
    gold = {tuple(sorted(pair)) for pair in gold_pairs}
    true_positive = len(predicted & gold)
    precision = true_positive / len(predicted) if predicted else 0.0
    recall = true_positive / len(gold) if gold else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"precision": precision, "recall": recall, "f1": f1,
            "true_positive": float(true_positive), "false_positive": float(len(predicted - gold)),
            "false_negative": float(len(gold - predicted))}
