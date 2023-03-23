import base64
import hashlib

from module import ROOT_DIR
from module.util.logger_conf import logger

FILENAME: str = ROOT_DIR + "/../data/test/intersect/collection_10000.txt"


def calculate_sha256(filename: str):
    hash_engine = hashlib.sha256()
    with open(file=filename, mode="rb") as f:
        buff = f.read()
        hash_engine.update(buff)
        pass
    hashed_value: bytes = hash_engine.digest()
    logger.info(f"hashed_value: {base64.b64encode(hashed_value).decode('utf-8')}")
    pass


def calculate_sha256_file_chunks(filename: str):
    buff_size: int = 256
    hash_engine = hashlib.sha256()
    with open(file=filename, mode="rb") as f:
        while buff := f.read(buff_size):
            hash_engine.update(buff)
            pass
        pass
    hashed_value: bytes = hash_engine.digest()
    logger.info(f"hashed_value: {base64.b64encode(hashed_value).decode('utf-8')}")
    pass


logger.info(f"===")
calculate_sha256(FILENAME)
calculate_sha256_file_chunks(FILENAME)
