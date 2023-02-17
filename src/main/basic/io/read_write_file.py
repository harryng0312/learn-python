
from io import FileIO


FILE_NAME: str = "data/matrix/mat1.txt"
FILE_NAME_2: str = "data/matrix/mat1_copy.txt"

def copy_file(srcFilePath: str, destFilePath: str):
    srcFile: FileIO
    destFile: FileIO
    buffSize: int = 1_024
    buffer: bytes = None
    try:
        with open(file = srcFilePath, mode = "+rb", buffering = buffSize) as srcFile, \
            open(file = destFilePath, mode = "+bw", buffering = buffSize) as destFile:
            # with open(file = destFilePath, mode = "+bw", buffering = buffSize) as destFile:
            buffer = srcFile.read(buffSize)
            while(buffer):
                destFile.write(buffer)
                destFile.flush()
                buffer = srcFile.read(buffSize)
    except Exception as ex:
        print(f"Exception: {ex}")
    finally:
        pass

print("copying...")
copy_file(FILE_NAME, FILE_NAME_2)