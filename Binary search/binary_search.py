numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,60]
def binary_search(list, item):
    low = 0
    high = len(list)-1
    counter = 1
    while low <= high:
        mid = (low+high)
        guess= list[mid]
        if guess == item:
            print("\nSteps: ",counter)
            counter=0
            return mid
        if guess > item:
            counter+=1
            high = mid - 1
        else:
            counter+=1
            low = mid+1
    return None

print(binary_search(numbers, 4))

print(binary_search(numbers, 16))