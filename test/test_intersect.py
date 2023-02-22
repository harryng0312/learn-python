import datetime
import random

SIZE = 1_000_000
FILE_NAME = f"./collection_{SIZE}.txt"


def gen_data():
    cA = random.sample(range(-SIZE * 10, SIZE * 10), SIZE)
    cB = random.sample(range(-SIZE * 10, SIZE * 10), SIZE)
    intersect = []
    tmpMap: dict = dict()
    # finTime: datetime
    # startTime: datetime = datetime.datetime.now()
    # print(f"start: {startTime}")
    for i in cA:
        tmpMap[i] = 0
        pass
    for i in cB:
        if i in tmpMap.keys():
            intersect.append(i)
            pass
        pass
    # finTime = datetime.datetime.now()
    # print(f"fin: {finTime}")
    # print(f"duration: {(finTime - startTime).microseconds}")
    # print(f"intersect:{intersect}")
    total: int = 0
    for i in intersect: total += i
    with open(file=FILE_NAME, mode="wt") as f:
        for i in cA: f.write(f"{i} ")
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
    cA = None
    cB = None
    mapTmp = set()
    intersect = []
    cTotalVal = 0
    # startTime: datetime = datetime.datetime.now()
    # print(f"start: {startTime}")
    with open(file=FILE_NAME, mode="rt") as f:
        strCA = f.readline()
        cA = [int(num.strip()) for num in strCA.split(" ") if num.strip() != ""]
        strCB = f.readline()
        cB = [int(num.strip()) for num in strCB.split(" ") if num.strip() != ""]
        pass
    # print(f"cA: {len(cA)}")
    # finTime = datetime.datetime.now()
    # print(f"fin: {finTime}")
    # print(f"duration: {(finTime - startTime).microseconds / 1000.0}")

    # startTime: datetime = datetime.datetime.now()
    # print(f"start: {startTime}")
    for i in cA:
        mapTmp.add(i)
        pass
    for i in cB:
        if i in mapTmp:
            intersect.append(i)
            cTotalVal += i
            pass
        pass
    print(f"{len(intersect)} {cTotalVal}")
    pass


def find_intersect2():
    cA = None
    cB = None
    cTotal = []
    with open(file=FILE_NAME, mode="rt") as f:
        strCA = f.readline()
        cA = [int(num.strip()) for num in strCA.split(" ") if num.strip() != ""]
        strCB = f.readline()
        cB = [int(num.strip()) for num in strCB.split(" ") if num.strip() != ""]
        pass

    intersect: list[int] = list()

    # startTime: datetime = datetime.datetime.now()
    # print(f"start: {startTime}")
    for i in cA: cTotal.append(i)
    for i in cB: cTotal.append(i)
    cTotal.sort()
    cTotalLen = len(cTotal)
    cTotalVal = 0
    for i in range(1, cTotalLen):
        if cTotal[i] == cTotal[i - 1]:
            intersect.append(cTotal[i])
            cTotalVal += cTotal[i]
            pass
        pass
    # finTime = datetime.datetime.now()
    # print(f"fin: {finTime}")
    # print(f"duration: {(finTime - startTime).microseconds / 1000.0}")
    print(f"{len(intersect)} {cTotalVal}")
    pass


def find_intersect3():
    cA = None
    cB = None
    # startTime: datetime = datetime.datetime.now()
    # print(f"start: {startTime}")
    with open(file=FILE_NAME, mode="rt") as f:
        strCA = f.readline()
        cA = [int(num) for num in strCA.split(" ") if num.strip() != ""]
        # arrCA = strCA.split(sep=" ")
        # for i in arrCA:
        #     if i.strip() != "":
        #         cA.append(int(i.strip()))
        #     pass
        strCB = f.readline()
        cB = [int(num) for num in strCB.split(" ") if num.strip() != ""]
        # arrCB = strCB.split(sep=" ")
        # for i in arrCB:
        #     if i.strip() != "":
        #         cB.append(int(i.strip()))
        #     pass
        pass

    intersect: list[int] = list()
    cTotalVal = 0

    # startTime: datetime = datetime.datetime.now()
    # print(f"start: {startTime}")
    for i in cA:
        for j in cB:
            if i == j:
                intersect.append(i)
                cTotalVal += i
            pass
    # finTime = datetime.datetime.now()
    # print(f"fin: {finTime}")
    # print(f"duration: {(finTime - startTime).microseconds / 1000.0}")
    print(f"{len(intersect)} {cTotalVal}")
    pass


# gen_data()
startTime = datetime.datetime.now()
print(f"start: {startTime}")
find_intersect1()
finTime = datetime.datetime.now()
print(f"fin: {finTime}")
print(f"duration: {(finTime - startTime).microseconds / 1000.0}")

print(f"======")
startTime = datetime.datetime.now()
print(f"start: {startTime}")
find_intersect2()
finTime = datetime.datetime.now()
print(f"fin: {finTime}")
print(f"duration: {(finTime - startTime).microseconds / 1000.0}")

# print(f"======")
# startTime = datetime.datetime.now()
# print(f"start: {startTime}")
# find_intersect3()
# finTime = datetime.datetime.now()
# print(f"fin: {finTime}")
# print(f"duration: {(finTime - startTime).microseconds / 1000.0}")
