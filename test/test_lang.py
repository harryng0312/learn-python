from datetime import datetime

uniStr: str = f"hi server máy chủ at:{ datetime.now() }"
uniBytes: bytes = bytes(uniStr, "utf-8")
print(f"result:{uniBytes.decode('utf-8')} len:{len(uniBytes)}")