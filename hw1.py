import random
import time
import matplotlib.pyplot as plt


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def measure_time(sort_func, arr, repeats=5):
    total = 0.0
    for _ in range(repeats):
        data = arr.copy()
        start = time.time()
        sort_func(data)
        total += time.time() - start
    return total / repeats


sizes = [100, 500, 1000, 2000, 5000, 7500, 10000, 20000]

repeats = 3
times_fast = []
times_slow = []

print("Измерение времени")
for n in sizes:
    arr = [random.randint(0, 10000) for _ in range(n)]

    t_fast = measure_time(merge_sort, arr, repeats)
    t_slow = measure_time(insertion_sort, arr, repeats)

    times_fast.append(t_fast)
    times_slow.append(t_slow)

    print(f"N = {n:5d} | Быстрая: {t_fast:.5f} с | Квадратичная: {t_slow:.5f} с")

plt.figure(figsize=(10, 6))
plt.plot(sizes, times_fast, 'o-', label='Сортировка слиянием (O(n log n))')
plt.plot(sizes, times_slow, 's-', label='Сортировка вставками (O(n²))')
plt.xlabel('Размер массива N')
plt.ylabel('Среднее время сортировки (секунды)')
plt.title('Сравнение времени сортировок')
plt.legend()
plt.grid(True)
plt.show()