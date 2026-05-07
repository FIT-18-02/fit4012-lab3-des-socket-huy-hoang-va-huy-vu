from des_socket_utils import encrypt_des_cbc, decrypt_des_cbc


def test_encrypt_decrypt_roundtrip():
    plain = b"Hello FIT4012"

    key, iv, cipher_bytes = encrypt_des_cbc(plain)

    decrypted = decrypt_des_cbc(key, iv, cipher_bytes)

    assert decrypted == plain