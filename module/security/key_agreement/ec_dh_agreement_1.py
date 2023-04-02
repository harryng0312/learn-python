from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey, EllipticCurvePublicKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
# Generate a private key for use in the exchange.
server_private_key: EllipticCurvePrivateKey = ec.generate_private_key(
    ec.SECP384R1()
)
server_public_key: EllipticCurvePublicKey = server_private_key.public_key()
# In a real handshake the peer is a remote client. For this
# example we'll generate another local private key though.
peer_private_key: EllipticCurvePrivateKey = ec.generate_private_key(
    ec.SECP384R1()
)
peer_public_key: EllipticCurvePublicKey = peer_private_key.public_key()

shared_key_at_server: bytes = server_private_key.exchange(algorithm=ec.ECDH(), peer_public_key=peer_public_key)
# Perform key derivation.
derived_key_at_server: HKDF = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(shared_key_at_server)
# And now we can demonstrate that the handshake performed in the
# opposite direction gives the same final value
shared_key_peer: bytes = peer_private_key.exchange(algorithm=ec.ECDH(), peer_public_key=server_public_key)
# Perform key derivation.
derived_key_at_peer: HKDF = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(shared_key_peer)
print(derived_key_at_server == derived_key_at_peer)