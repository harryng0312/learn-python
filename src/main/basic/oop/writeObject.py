import pickle
import os
from Person import *

PERSON_FILE_PATH = "data/person/student.dat"

def writeToBinFile(x: Student):
    with open(file=PERSON_FILE_PATH, buffering=1024, mode="+bw") as destFile:
        xData: bytes = pickle.dumps(obj=x)
        destFile.write(xData)
        destFile.flush
    pass


def readFromBinFile():
    with open(file=PERSON_FILE_PATH, buffering=1024, mode="+br") as destFile:
        destFile.seek(0, os.SEEK_END)
        endPos: int = destFile.tell()
        destFile.seek(0, 0)
        xData: bytes = destFile.read(endPos)
        x:Student = pickle.loads(xData)
        # x: Student = pickle.load(destFile)
        print(f"Student:{x}")
    pass

x: Student = Student("Mike", "Olsen", 2019)
writeToBinFile(x)
readFromBinFile()
