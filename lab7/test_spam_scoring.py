
from hypothesis import given, strategies as st
from spam_scoring import sender_domain, first_link, shout_ratio


# Test 1: Sender domain should not crash
@given(st.text() | st.none())
def test_sender_domain_no_crash(s):
    sender_domain(s)


# Test 2: First link should not crash
@given(st.text() | st.none())
def test_first_link_no_crash(s):
    first_link(s)


# Test 3: Shout ratio should not crash
@given(st.text() | st.none())
def test_shout_ratio_no_crash(s):
    shout_ratio(s)
