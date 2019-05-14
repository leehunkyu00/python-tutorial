# https://wayhome25.github.io/python/2017/02/24/py-07-for-loop/

def samplefor1(arr):
    print("sample for 1")
    for v in arr:
        print(v)

def samplefor2(arr):
    print("sample for 2")

    length = len(arr)
    for i in range(length):
        print(arr[i])

def samplefor3(arr):
    print("sample for 3")

    for i, character in enumerate(arr):
        print(i, character)

testArr = ['a', 'b', 'c', 'd', 'e']

samplefor1(testArr)
samplefor2(testArr)
samplefor3(testArr)