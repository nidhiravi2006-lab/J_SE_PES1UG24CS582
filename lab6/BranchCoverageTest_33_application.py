
from spam_scoring import (
    score_message,
    classify,
    filter_inbox,
    inbox_status
)


def test_spam_word_branch():
    assert score_message("free WINNER!", False, 0) == 4


def test_uppercase_branch():
    assert score_message("HELLO", False, 0) == 1


def test_normal_word_branch():
    assert score_message("hello", False, 0) == 0


def test_short_uppercase_branch():
    assert score_message("HI", False, 0) == 0


def test_link_more_than_three():
    assert score_message("hello", False, 4) == 4


def test_link_between_one_and_three():
    assert score_message("hello", False, 1) == 1


def test_zero_links():
    assert score_message("hello", False, 0) == 0


def test_known_sender_positive_score():
    assert score_message("free winner", True, 0) == 1


def test_known_sender_negative_score():
    assert score_message("hello", True, 0) == 0


def test_unknown_sender():
    assert score_message("free", False, 0) == 2


def test_classify_spam_boundary():
    assert classify(8) == "spam"


def test_classify_suspicious_boundary():
    assert classify(4) == "suspicious"


def test_classify_clean_boundary():
    assert classify(3) == "clean"


def test_filter_empty_inbox():
    assert filter_inbox([]) == {
        "spam": 0,
        "suspicious": 0,
        "clean": 0
    }


def test_filter_mixed_inbox():
    messages = [
        ("free winner prize urgent", False, 0),
        ("free winner", False, 0),
        ("hello", False, 0)
    ]
    assert filter_inbox(messages) == {
        "spam": 1,
        "suspicious": 1,
        "clean": 1
    }


def test_inbox_empty():
    assert inbox_status({
        "spam": 0, "suspicious": 0, "clean": 0
    }) == "empty"


def test_inbox_flooded():
    assert inbox_status({
        "spam": 6, "suspicious": 2, "clean": 2
    }) == "flooded"


def test_inbox_noisy():
    assert inbox_status({
        "spam": 3, "suspicious": 4, "clean": 3
    }) == "noisy"


def test_inbox_healthy():
    assert inbox_status({
        "spam": 1, "suspicious": 3, "clean": 6
    }) == "healthy"


def test_inbox_ratio_boundary():
    assert inbox_status({
        "spam": 2, "suspicious": 3, "clean": 5
    }) == "healthy"


def test_inbox_half_spam():
    assert inbox_status({
        "spam": 5, "suspicious": 2, "clean": 3
    }) == "noisy"
