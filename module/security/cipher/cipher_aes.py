import os
import base64
from module.util.logger_conf import logger
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers import Cipher, CipherContext, algorithms, modes


def genSecretKey(keyLength: int, needAdd: bool) -> tuple[bytes, bytes, bytes]:
    key: bytes = os.urandom(keyLength)
    iv: bytes = os.urandom(keyLength)
    add: bytes = None
    if needAdd:
        add = os.urandom(keyLength)
        pass
    return key, iv, add

def encrypt(key: bytes, iv: bytes, add: bytes, data: bytes) -> tuple[bytes, bytes]:
    cipher: Cipher = Cipher(algorithm=algorithms.AES(key), \
                            mode=modes.GCM(initialization_vector=iv))
    encryptor: CipherContext = cipher.encryptor()
    result: bytearray = bytearray()
    encryptor.authenticate_additional_data(add)
    result += encryptor.update(data=data)
    result += encryptor.finalize()
    tag: bytes = encryptor.tag
    return result, tag

def decrypt(key: bytes, iv: bytes, add: bytes, tag: bytes, data: bytes) -> bytes:
    cipher: Cipher = Cipher(algorithm=algorithms.AES(key), \
                            mode=modes.GCM(initialization_vector=iv, tag=tag))
    decryptor: CipherContext = cipher.decryptor()
    result: bytearray = bytearray()
    decryptor.authenticate_additional_data(add)
    result += decryptor.update(data=data)
    result += decryptor.finalize()
    return result


plain_data: bytes = b"test try again"
logger.info(f"plain data:{base64.b64encode(s=plain_data).decode('utf-8')}")
key, iv, add = genSecretKey(16, True)

crypted_data, tag = encrypt(key=key, iv=iv, add=add, data=plain_data)
logger.info(f"encrypted base64:{base64.b64encode(s=crypted_data).decode('utf-8')} tag:{base64.b64encode(s=tag).decode('utf-8')}")
try:
    replain_data: bytes = decrypt(key=key, iv=iv, add=add, tag=tag, data=crypted_data)
    logger.info(f"decrypted base64:{base64.b64encode(s=replain_data).decode('utf-8')}")
    pass
except (InvalidTag, TypeError) as ex:
    # logger.error("", ex)
    pass

