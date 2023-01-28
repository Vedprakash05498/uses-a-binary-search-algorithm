# In this code, 
we first defined a function binary_search(arr, x) which takes in a list arr and a number x as input and returns the index of x in the list
if it is present, otherwise it returns -1.
Then we created a list of random numbers between 0 to 100 with every succeeding number having a difference of 2 using list comprehension.
Then we take input from the user and store it in the variable x.
After that, we call the binary_search function by passing the list and x as arguments and store the returned value in the variable result.
Finally, we check if the number is in the list or not by comparing the value of result with -1. If it's not -1, then the number is in the list, 
otherwise it's not.






import random

def binary_search(arr, x):
    # initialize the start and end index of the array
    start = 0
    end = len(arr) - 1

    # loop until the subarray size becomes 0
    while start <= end:
        # calculate the middle index
        mid = (start + end) // 2
        
        # check if x matches with the middle element
        if arr[mid] == x:
            return mid
        
        # if x is greater than the mid element, search in the right half
        elif arr[mid] < x:
            start = mid + 1
        
        # if x is smaller, search in the left half
        else:
            end = mid - 1
    
    # if x is not found in the array
    return -1

# create a list of random numbers between 0 to 100, with every succeeding number having a difference of 2
arr = [i*2 for i in range(0, 51)]

# input a random number from the user
x = int(input("Enter a number between 0 to 100: "))

# call the binary search function
result = binary_search(arr, x)

# check if the number is in the list
if result != -1:
    print("The number is in the list at index:", result)
else:
    print("The number is not in the list.")
