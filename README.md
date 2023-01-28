# Uses-of-binary-search-algorithm

In summary, the task is to create a Python program that uses a binary search algorithm to search for a user-inputted number in a list of randomly generated numbers between 0 and 100, with a difference of 2 between each number. The program will divide the list into halves and continue narrowing the search until the number is found or the subarray size becomes 0. The program should be written in a Jupyter notebook and submitted as an ipynb file. The data will be input from the user, and it is important to use proper code blocks, comments, and insights while writing the code. Additionally, it is important to only use the variable names mentioned in the instructions and to check the data frame after performing each set of operations.





# Hints:

Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.


# Approach

Create a list of random numbers between 0 and 100, with every succeeding number having a difference of 2 between them.
Prompt the user to input a number to search for in the list.
Implement a binary search algorithm to find the user's input in the list.
Compare the user's input with the middle element of the list.
If the input matches the middle element, return the index of the middle element.
If the input is greater than the middle element, search the right half of the list.
If the input is smaller than the middle element, search the left half of the list.
If the subarray size becomes 0, return that the input is not in the list.
