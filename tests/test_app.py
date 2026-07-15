from app import build_message


def test_build_message():
    assert "Application" in build_message()
