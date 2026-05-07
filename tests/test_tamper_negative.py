import pytest
from des_socket_utils import encrypt_des_cbc, decrypt_des_cbc

def test_tampered_ciphertext_should_fail():
    plain = b"FIT4012"

    key, iv, cipher_bytes = encrypt_des_cbc(plain)

    tampered = bytearray(cipher_bytes)
    tampered[0] ^= 0xFF

    with pytest.raises(Exception):
        decrypt_des_cbc(key, iv, bytes(tampered))