import datetime
import random

SIZE = 1_000_000
FILE_NAME = f"./collection_{SIZE}.txt"


def gen_data():
    cA = random.sample(range(-SIZE * 10, SIZE * 10), SIZE)
    cB = random.sample(range(-SIZE * 10, SIZE * 10), SIZE)
    intersect: list[int] = list()
    tmpMap: dict = dict()
    print(f"start: {datetime.datetime.now()}")
    for i in cA:
        tmpMap[i] = 0
        pass
    for i in cB:
        if i in tmpMap.keys():
            intersect.append(i)
            pass
        pass
    print(f"fin: {datetime.datetime.now()}")
    # print(f"intersect:{intersect}")
    total: int = 0
    for i in intersect: total += i
    with open(file=FILE_NAME, mode="wt") as f:
        for i in cA: f.write(f"{i} "); pass
        f.write("\n")
        f.flush()
        for i in cB: f.write(f"{i} ")
        f.write("\n")
        f.flush()
        f.write(f"{len(intersect)} {total}")
        f.flush()
        pass
    pass


def find_intersect1():
    cA = []
    cB = []
    with open(file=FILE_NAME, mode="rt") as f:
        strCA = f.readline()
        arrCA = strCA.split(sep=" ")
        for i in arrCA:
            if i.strip() != "":
                cA.append(int(i.strip()))
            pass
        strCB = f.readline()
        arrCB = strCB.split(sep=" ")
        for i in arrCB:
            if i.strip() != "":
                cB.append(int(i.strip()))
            pass
        pass

    intersect: list[int] = list()
    mapTmp = set()
    cTotalVal = 0
    print(f"start: {datetime.datetime.now()}")
    for i in cA:
        mapTmp.add(i)
        pass
    for i in cB:
        if i in mapTmp:
            intersect.append(i)
            cTotalVal += i
            pass
        pass
    print(f"fin: {datetime.datetime.now()}")
    print(f"{len(intersect)} {cTotalVal}")
    pass


def find_intersect2():
    cA = []
    cB = []
    with open(file=FILE_NAME, mode="rt") as f:
        strCA = f.readline()
        arrCA = strCA.split(sep=" ")
        for i in arrCA:
            if i.strip() != "":
                cA.append(int(i.strip()))
            pass
        strCB = f.readline()
        arrCB = strCB.split(sep=" ")
        for i in arrCB:
            if i.strip() != "":
                cB.append(int(i.strip()))
            pass
        pass

    intersect: list[int] = list()
    cTotal = []
    print(f"start: {datetime.datetime.now()}")
    for i in cA:
        cTotal.append(i)
        pass
    for i in cB:
        cTotal.append(i)
        pass
    cTotal.sort()
    cTotalLen = len(cTotal)
    cTotalVal = 0
    for i in range(1, cTotalLen):
        if cTotal[i] == cTotal[i - 1]:
            intersect.append(cTotal[i])
            cTotalVal += cTotal[i]
            pass
        pass
    print(f"fin: {datetime.datetime.now()}")
    print(f"{len(intersect)} {cTotalVal}")
    pass


# gen_data()
find_intersect1()
