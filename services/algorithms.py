def linear_search(data, key):
    for d in data:
        if d.nim == key:
            return d
    return None

def insertion_sort(data):
    arr = data[:]
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1].nim > arr[j].nim:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr
