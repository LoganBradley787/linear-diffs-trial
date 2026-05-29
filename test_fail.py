from app import add


def test_fail():
    assert add(2, 3) == 6  # intentionally wrong -> CI red
