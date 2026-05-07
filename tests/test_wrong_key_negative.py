import os
import pytest
from des_socket_utils import encrypt_des_cbc, decrypt_des_cbc

def test_wrong_key_should_fail():
    plain = b"Secret Message"

    key, iv, cipher_bytes = encrypt_des_cbc(plain)

    wrong_key = os.urandom(8)

    with pytest.raises(Exception):
        decrypt_des_cbc(wrong_key, iv, cipher_bytes)