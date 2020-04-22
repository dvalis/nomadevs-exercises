## Exercise 2 "Implement the function find_minimum(A) which returns the minimum value of array A. For example, given the array [4, 10, 40, -5, 100, -43] the function would return -43."

def find_minimum(A):
    if len(A) == 0:             
        return None
    minimum = A[0]              
    for i in range(1, len(A)):  
        if A[i] < minimum:      
            minimum = A[i]       
    return minimum


A = [4, 10, 40, -5, 100, -43]
print('Minimum of', A, 'is', find_minimum(A))


## Exercise 3 "Implement the function calculate_average(A) which returns the average value of elements of array A. For example, given the array [30, 20, 10, 40] the function would return 25."

def average(A):
    if len(A) == 0:             
        return None
    sum = 0
    for i in range(0, len(A)):
        sum = sum + A[i]
    average = sum / len(A)
    return average

A = [30, 20, 10, 40]
print('Average of all the elements of the array is', average(A))

## Exercise 4 "Implement the function is_symmetrical(A) which returns True if the array A is symmetrical or False otherwise. For example, given the array [10, 20, 20, 10] or [10, 0, 5, 0, 10] the function would return True, whereas given the array [10, 0, 4, -5, 10] it would return False."


def is_symmetrical(A):
    if not A:
        return False
    for i in range(len(A) / 2):
            if A[i] != A[len(A) - 1 - i]:
        return False
    return True
A = [10, 20, 20, 10]
isA = is_symmetrical(A) # TrueNomadevs
2 / 3
B = [10, 0, 5, 0, 10]
isB = is_symmetrical(B) # True
C = [10, 0, 4, -5, 10]
isC = is_symmetrical(C) # False


## Exercise 5 "The best-case time complexity of the given bubble sort implementation is Ω(n²) since the algorithmwill continue to make comparisons even if the array is sorted beforehand. Can you think of a little
## tweak to optimize bubble sort and achieve the best-case time complexity of Ω(n)? To optimize our bubble sort algorithm, we can introduce a flag to monitor whether elements are
## getting swapped inside the inner for-loop. Hence, in the inner for-loop, we check whether swapping of elements is taking place or not, everytime. If for a particular iteration, no swapping took place, it means 
## the array has been sorted and we can jump out of the for-loop, instead of executing all the iterations. So, if array A is already sorted then in one iteration we exit the function. Thus, we achieve the complexity Ω(n)." 

def bubblesort(A):
    for i in reversed(range(1, len(A))):
        for j in range(0, i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp    

A = [60, 61, 50, 62]

bubblesort(A)
print('After:', A)

## Exercise 7 "Implement the function calculate_median(A) which returns the median value of elements of array A. The median of a sorted array of size n is defined as the middle element when n is odd and average 
# of middle two elements when n is even. For example, given the array [5, 50, 60, 61, 62] the function would return 60. However, array A might not be sorted "

def bubblesort(A):
    for i in reversed(range(1, len(A))):
        for j in range(0, i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp    

A = [60, 61, 50, 62]

bubblesort(A)
print('After:', A)

def calcualte_median(A):
    
    if len(A) % 2 == 0:
        return (A[int(len(A) / 2)] + A[int(len(A) / 2 - 1)]) / 2
    else:
        return A[int(len(A) / 2)]

print(calcualte_median(A))

B = [60, 61, 50, 62, 5]
bubblesort(B)
print('After:', B)

print(calcualte_median(B))


## Exercise 8 "Implement the function is_there_sum(A, target) which return True if there exists two elements in A whose sum is exactly target or False otherwise"

A = [30, 20, 10, 40]

target = int(input())
def is_there_sum(A, target):
    if len(A) == 0:       
        return None
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if A[j] + A[i] == target:
                return True
            
    return False

print(is_there_sum(A, target))

## Exercise 9 "Implement the function rotate(A, count) which rotates the array A by count elements. For example, given the array [1, 2, 3, 4, 5, 6, 7] and count = 2 the function would return [3, 4, 5, 6, 7, 1, 2]."

def rotate_once(A):
    if not A:
        return

    temp = A[0]

    for i in range(len(A) - 1):
        A[i] = A[i+1]

    A[len(A) - 1] = temp

def rotate(A, count):
    if not A:
        return
    for i in range(count):
        rotate_once(A)

A = [1, 2, 3, 4, 5, 6, 7]
rotate(A, 2) 



