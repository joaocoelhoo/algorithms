from pytest import raises
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    message = "CUSCUZ"

    first_case = "SUC_ZUC"
    second_case = "ZU_CSUC"
    third_case = "ZUCSUC"

    assert encrypt_message(message, 3) == first_case
    assert encrypt_message(message, 4) == second_case
    assert encrypt_message(message, -1) == third_case

    with raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message, "doritos")
    with raises(TypeError, match="tipo inválido para message"):
        encrypt_message(10, 4)
