import datetime
import random
from concurrent.futures import ThreadPoolExecutor

from module import ROOT_DIR

SIZE = 10_000
FILE_NAME = ROOT_DIR + f"/../data/test/intersect/collection_{SIZE}.txt"


def gen_data():
    cA = random.sample(range(-SIZE * 10, SIZE * 10), SIZE)
    cB = random.sample(range(-SIZE * 10, SIZE * 10), SIZE)
    intersect = []
    tmpMap: dict = dict()
    for i in cA:
        tmpMap[i] = 0
        pass
    for i in cB:
        if i in tmpMap.keys():
            intersect.append(i)
            pass
        pass
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


def find_intersect_hashset():
    cA = None
    cB = None
    mapTmp = set()
    intersect = []
    cTotalVal = 0
    # startTimeIn = datetime.datetime.now()
    with open(file=FILE_NAME, mode="rt") as f:
        strCA = f.readline().split(" ")
        cA = [int(num.strip()) for num in strCA if num.strip() != ""]
        strCB = f.readline().split(" ")
        cB = [int(num.strip()) for num in strCB if num.strip() != ""]
        pass
    # finTimeIn = datetime.datetime.now()
    # print(f"duration internal: {(finTimeIn - startTimeIn).total_second()}")
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


def find_intersect_mergeandsort():
    cA = None
    cB = None
    cTotal = []
    # startTimeIn = datetime.datetime.now()
    # print(f"start internal: {startTimeIn}")
    with open(file=FILE_NAME, mode="rt") as f:
        strCA = f.readline().split(" ")
        cA = [int(num.strip()) for num in strCA if num.strip() != ""]
        strCB = f.readline().split(" ")
        cB = [int(num.strip()) for num in strCB if num.strip() != ""]
        pass
    # finTimeIn = datetime.datetime.now()
    # print(f"fin internal: {finTimeIn}")
    # print(f"duration internal: {(finTimeIn - startTimeIn).total_seconds()}")
    intersect: list[int] = list()
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
    print(f"{len(intersect)} {cTotalVal}")
    pass


def find_intersect_tradition():
    cA = None
    cB = None
    with open(file=FILE_NAME, mode="rt") as f:
        strCA = f.readline().split(" ")
        cA = [int(num) for num in strCA if num.strip() != ""]
        strCB = f.readline().split(" ")
        cB = [int(num) for num in strCB if num.strip() != ""]
        pass
    intersect = []
    cTotalVal = 0
    for i in cA:
        for j in cB:
            if i == j:
                intersect.append(i)
                cTotalVal += i
                break
            pass
    print(f"{len(intersect)} {cTotalVal}")
    pass


def compare_value_in_range(val: int, arr: [int]) -> ([], int):
    tmpIntersect = []
    cTotalValTmp = 0
    for v in arr:
        if val == v:
            tmpIntersect.append(val)
            # with lock:
            #     res.append(val)
            cTotalValTmp += val
            break
        pass
    return tmpIntersect, cTotalValTmp


def find_intersect_tradition_parallel():
    cA: [int] = None
    cB: [int] = None
    with open(file=FILE_NAME, mode="rt") as f:
        strCA = f.readline().split(" ")
        cA = [int(num) for num in strCA if num.strip() != ""]
        strCB = f.readline().split(" ")
        cB = [int(num) for num in strCB if num.strip() != ""]
        pass
    intersect = []
    cTotalVal = 0
    ccB = (cB for _ in cA)
    # res = (intersect for _ in cA)
    with ThreadPoolExecutor(max_workers=SIZE//10) as executor:
        for iterTmp, tmpTotalVal in executor.map(compare_value_in_range, cA, ccB):
            intersect.extend(iterTmp)
            cTotalVal += tmpTotalVal
            pass
        pass
    print(f"{len(intersect)} {cTotalVal}")
    pass


def find_intersect_tradition_parallel_queue():
    cA: [int] = None
    cB: [int] = None
    with open(file=FILE_NAME, mode="rt") as f:
        strCA = f.readline().split(" ")
        cA = [int(num) for num in strCA if num.strip() != ""]
        strCB = f.readline().split(" ")
        cB = [int(num) for num in strCB if num.strip() != ""]
        pass
    intersect = []
    cTotalVal = 0
    ccB = (cB for _ in cA)
    # res = (intersect for _ in cA)
    with ThreadPoolExecutor(max_workers=SIZE//100) as executor:
        for iterTmp, tmpTotalVal in executor.map(compare_value_in_range, cA, ccB):
            intersect.extend(iterTmp)
            cTotalVal += tmpTotalVal
            pass
        pass
    print(f"{len(intersect)} {cTotalVal}")
    pass


# gen_data()
startTime1 = datetime.datetime.now()
print(f"start: {startTime1}")
find_intersect_hashset()
finTime1 = datetime.datetime.now()
print(f"fin: {finTime1}")
print(f"duration: {(finTime1 - startTime1).total_seconds()}")

print(f"======")
startTime2 = datetime.datetime.now()
print(f"start: {startTime2}")
find_intersect_mergeandsort()
finTime2 = datetime.datetime.now()
print(f"fin: {finTime2}")
print(f"duration: {(finTime2 - startTime2).total_seconds()}")

print(f"======")
startTime = datetime.datetime.now()
print(f"start: {startTime}")
find_intersect_tradition()
finTime = datetime.datetime.now()
print(f"fin: {finTime}")
print(f"duration: {(finTime - startTime).total_seconds()}")

# print(f"======")
# startTime = datetime.datetime.now()
# print(f"start: {startTime}")
# find_intersect_tradition_parallel()
# finTime = datetime.datetime.now()
# print(f"fin: {finTime}")
# print(f"duration: {(finTime - startTime).total_seconds()}")

print(f"======")
startTime = datetime.datetime.now()
print(f"start: {startTime}")
find_intersect_tradition_parallel_queue()
finTime = datetime.datetime.now()
print(f"fin: {finTime}")
print(f"duration: {(finTime - startTime).total_seconds()}")
