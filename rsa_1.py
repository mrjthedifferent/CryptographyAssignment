from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


class MixNode:
    def __init__(self, private_key, next_node=None):
        self.private_key = private_key
        self.next_node = next_node

    def decrypt_message(self, ciphertext):
        plaintext = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext

    def mix(self, ciphertext):
        # Mixnet logic goes here
        # For simplicity, we just pass the ciphertext to the next node
        if self.next_node:
            return self.next_node.mix(ciphertext)
        else:
            return ciphertext


# Key generation
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Serialize public key for sharing
serialized_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Create mix nodes
mix_node_3 = MixNode(private_key, next_node=None)
mix_node_2 = MixNode(private_key, next_node=mix_node_3)
mix_node_1 = MixNode(private_key, next_node=mix_node_2)

# Encrypt a message with the public key
message = b"Hello, mixnet with RSA!"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Start mixing process
result = mix_node_1.mix(ciphertext)

# Decrypt the final result
decrypted_result = mix_node_3.decrypt_message(result)
print("Decrypted Result:", decrypted_result.decode('utf-8'))
