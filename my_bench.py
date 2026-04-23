import bench
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(a):
    for i in range(len(a)):
        lowest_number_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[lowest_number_idx]:
                lowest_number_idx = j
        a[i], a[lowest_number_idx] = a[lowest_number_idx], a[i] # vertauschen

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
def csv_show(name, N, ncomp, rtime):
    with open("results.csv", "a") as f:
        f.write(f"{name},{N},{ncomp},{rtime}\n")

def table_show(name, N, ncomp, rtime):
    print(f"{name:15} | {N:10} | {ncomp:15} | {rtime:10}ms")

bench.add_algo("bubblesort",bubble_sort)


# Sammle Ergebnisse
results = {}

for N in (100,500,1000, 2000):
    bench.do_run("random", "built_in", "simple_show", N)
    bench.do_run("random", "bubblesort", "simple_show", N)
