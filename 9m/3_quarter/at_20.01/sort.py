def sort(arr):
    n = len(arr)
    if n <= 1:
        return -1
    for i in range(1, n):
        now = arr[i]
        j = i - 1
        while j >= 0 and now < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = now
    return arr

m = int(input("Введите число элементов массива "))
arr = []

for i in range(m):
    arr.append(int(input()))
print(sort(arr))
