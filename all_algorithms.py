import time

my_list = []
THRESHOLD = 100

def size_selection():
    size_selection = int(input("\nPlease enter the random array size\n"+
                                "Available ones:\n"+
                                "100, 1_000, 10_000, 100_000, 1_000_000 (not available Quick Sort)\n"+
                                "7250, 7500, 11500, 800000\n"))
    return size_selection

def algo_selection():
    algorithm_selection = int(input("\nPlease enter algorithm you want to use\n"+
                            "1 - Selection Sort\n"+
                            "2 - Bubble Sort\n"+
                            "3 - Merge Sort\n"+
                            "4 - Quick Sort\n"+
                            "5 - Improved Bubble Sort\n"+
                            "6 - Improved Quick Sort\n"+
                            "Improved Bubble Sort: Better if you have kind of sorted array\n"+
                            "Improved Quick Sort: Uses Selection Sort for the size less than 100\n"))
        
    return algorithm_selection


def file_reader(size):
    global my_list
    rand_sort = int(input("\nDo you want sorted or random array\n"+
                          "1 - Sorted Array\n"+
                          "2 - Random Array\n"))
    if rand_sort == 1:
        with open("sorted_numbers{}.txt".format(size), "r") as file:
            numbers = file.read().split()

        my_list = [int(num) for num in numbers]
    elif rand_sort == 2:
        with open("random_numbers{}.txt".format(size), "r") as file:
            numbers = file.read().split()

        my_list = [int(num) for num in numbers]


def selectionSort(test_list):
    for i in range(0, len(test_list)):
        min_index = i
        for j in range(i+1, len(test_list)):
            if test_list[min_index] > test_list[j]:
                min_index = j
        temp = test_list[i]
        test_list[i] = test_list[min_index]
        test_list[min_index] = temp
    return test_list


def bubbleSort(test_list):
    n = len(test_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if test_list[j] > test_list[j+1]:
                test_list[j], test_list[j+1] = test_list[j+1], test_list[j]
    return test_list


def merge(A, B, C):
    i = 0
    j = 0
    k = 0

    while i<len(B) and j<len(C):
        if B[i] <= C[j]:
            A[k] = B[i]
            i+=1
        else:
            A[k] = C[j]
            j+=1
        k+=1

    while i < len(B):
        A[k] = B[i]
        i += 1
        k += 1

    while j < len(C):
        A[k] = C[j]
        j += 1
        k += 1


def mergeSort(A):
    if len(A)>1:
        mid = len(A)//2
        B = A[:mid]
        C = A[mid:]
        mergeSort(B)
        mergeSort(C)
        merge(A,B,C)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


def bubbleSortImproved(test_list):
    n = len(test_list)
    for i in range(n):
        sorted = True
        for j in range(0, n-i-1):
            if test_list[j] > test_list[j+1]:
                test_list[j], test_list[j+1] = test_list[j+1], test_list[j]
                sorted = False
        if sorted:
            break
    return test_list


def quick_sort_improved(test_list):
    if len(test_list) <= THRESHOLD:
        return selectionSort(test_list)
    else:
        if len(test_list) <= 1:
            return test_list
        else:
            pivot = test_list[0]
            less_than_pivot = [x for x in test_list[1:] if x <= pivot]
            greater_than_pivot = [x for x in test_list[1:] if x > pivot]
            return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

while True:
    try:
        size = size_selection()
        match size:
            case 100:
                file_reader(size=100)
            case 1_000:
                file_reader(size=1_000)
            case 7_250:
                file_reader(size=7_250)
            case 7_500:
                file_reader(size=7_500)
            case 10_000:
                file_reader(size=10_000)
            case 11_500:
                file_reader(size=11_500)
            case 100_000:
                file_reader(size=100_000)
            case 850_000:
                file_reader(size=850_000)
            case 1_000_000:
                file_reader(size=1_000_000)
            case _:
                print("You entered something wrong!")
    except:
        print("Enter Again!")
    else:
        break

while True:
    try:
        algo_num = algo_selection()
        match algo_num:
            case 1:
                start = time.time()
                sortedList = selectionSort(my_list)
                end = time.time()
                timeTaken = end-start
                print("Sorted List:", sortedList)
                print("Time taken for Selection Sort with", len(my_list), "input size is:", timeTaken, "Seconds")
            case 2:
                start = time.time()
                sortedList = bubbleSort(my_list)
                end = time.time()
                timeTaken = end-start
                print("Sorted List:", sortedList)
                print("Time taken for Bubble Sort with", len(my_list), "input size is:", timeTaken, "Seconds")
            case 3:
                start = time.time()
                mergeSort(my_list)
                end = time.time()
                timeTaken = end-start
                print("Sorted List:", my_list)
                print("Time taken for Merge Sort with", len(my_list), "input size is:", timeTaken, "Seconds")
            case 4:
                start = time.time()
                sortedList = quick_sort(my_list)
                end = time.time()
                timeTaken = end-start
                print("Sorted List:", sortedList)
                print("Time taken for Quick Sort with", len(my_list), "input size is:", timeTaken, "Seconds")
            case 5:
                start = time.time()
                sortedList = bubbleSortImproved(my_list)
                end = time.time()
                timeTaken = end-start
                print("Originally Sorted list to Sorted List:", sortedList)
                print("Time taken for Improved Bubble Sort with Sorted List", len(my_list), "input size is:", timeTaken, "Seconds")
            case 6:
                start = time.time()
                quick_sort_improved(my_list)
                end = time.time()
                timeTaken = end-start
                print("Sorted List:", my_list)
                if len(my_list) > THRESHOLD:
                    print("Time taken for Improved Quick Sort with", len(my_list), "input size is:", timeTaken, "Seconds")
                else:
                    print("Due to Threshold, Selection Sort was used.")
                    print("Time taken for Improved Quick Sort with", len(my_list), "input size is:", timeTaken, "Seconds")
            case _:
                print("You entered something wrong!")
                algo_selection()
    except:
        print("Enter Again!")
    else:
        break