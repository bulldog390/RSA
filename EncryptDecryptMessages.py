import rsa

def encrypt_rsa(public_key, message):
    pubkey = rsa.PublicKey.load_pkcs1(public_key)
    encrypted = rsa.encrypt(message.encode(), pubkey)
    return encrypted

public_key = b'-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAp+L/jJ1q3W8NQz/TKg1MvB9jtW8HZbN+oJysl04TfTzTlK+Bm7tT\ndvbPXJn8/UdV7jJibOv+V7wL8A0NOaFhMzPyf9+zM/Go1A55ZQbL1g0xR6wH8BJj\nU5E6U5V9UqrO+H/Nxw5M1ZNgQ2Fh/r3q1z6/5U6YhUoLzv7Vcxp/bZh7VuVRms/l\nXB2QIDAQAB\n-----END RSA PUBLIC KEY-----'
message = "hello world"
encrypted = encrypt_rsa(public_key, message)
print(encrypted)


import rsa

def decrypt_rsa(private_key, encrypted_message):
    privkey = rsa.PrivateKey.load_pkcs1(private_key)
    decrypted = rsa.decrypt(encrypted_message, privkey).decode()
    return decrypted

private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAp+L/jJ1q3W8NQz/TKg1MvB9jtW8HZbN+oJysl04TfTzTlK+B\nm7tTdvbPXJn8/UdV7jJibOv+V7wL8A0NOaFhMzPyf9+zM/Go1A55ZQbL1g0xR6wH\n8BJjU5E6U5V9UqrO+H/Nxw5M1ZNgQ2Fh/r3q1z6/5U6YhUoLzv7Vcxp/bZh7VuVRm\ns/lXB2QIDAQABAoIBAAxA8WfAKzSGvuvBKjbzsCfBTTlEZxpCjK9XxLebabz8WdR\ngvzfjrKwgAq8WqcL1v2QxaLkxjKj5UO/N1jQPD/S7/P5AD6CZjG/N/N4f7IpOJjf\nspyhMCCzL0V/M0mZK7Vmv9GEuX7x0mjJn
