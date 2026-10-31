
from spam_scoring import (
    score_message,
    classify,
    filter_inbox,
    inbox_status,
)


def test_spam_words():
    assert score_message("free winner prize", False, 0) == 6


def test_uppercase_words():
    assert score_message("HELLO WORLD", False, 0) == 2


def test_many_links():
    assert score_message("hello", False, 5) == 4


def test_few_links():
    assert score_message("hello", False, 2) == 1


def test_known_sender():
    assert score_message("free winner", True, 0) == 1


def test_known_sender_negative_score():
    assert score_message("hello", True, 0) == 0


def test_classify_spam():
    assert classify(8) == "spam"


def test_classify_suspicious():
    assert classify(5) == "suspicious"


def test_classify_clean():
    assert classify(0) == "clean"


def test_filter_inbox():
    messages = [
        ("free winner prize urgent", False, 0),
        ("free winner", False, 0),
        ("hello", False, 0),
    ]
    assert filter_inbox(messages) == {
        "spam": 1,
        "suspicious": 1,
        "clean": 1,
    }


def test_empty_inbox():
    assert inbox_status({
        "spam": 0, "suspicious": 0, "clean": 0
    }) == "empty"


def test_flooded_inbox():
    assert inbox_status({
        "spam": 6, "suspicious": 2, "clean": 2
    }) == "flooded"


def test_noisy_inbox():
    assert inbox_status({
        "spam": 3, "suspicious": 4, "clean": 3
    }) == "noisy"


def test_healthy_inbox():
    assert inbox_status({
        "spam": 1, "suspicious": 3, "clean": 6
    }) == "healthy"
