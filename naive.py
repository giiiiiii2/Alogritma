# naive.py
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    import random  

    random.seed(40)
    data = [random.randint(0, 100) for _ in range(50)]

    print("Data asli:", data)  
    sorted_data = bubble_sort(data) 
    print("Data setelah disorting (naive):", sorted_data)  
