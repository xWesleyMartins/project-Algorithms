from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 123)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("test_message", "test_key")

    assert encrypt_message("minecraft", 3) == "nim_tfarce"
    assert encrypt_message("darksiders", 4) == "sredis_krad"
    assert encrypt_message("bioshock", 10) == "kcohsoib"
