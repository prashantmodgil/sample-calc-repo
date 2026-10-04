def bubble_sort(arr:list)->list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def add(a:int,b:int)->int:
    return a+b

def process_map(map:dict)->list:
    return list(map.values())