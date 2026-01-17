# Compliment Search

This program generates a list of (default) 10000 integers.  It uses three different algorithms to look at the first integer in a sorted list, and determine if it's compliment (negated value) exists. Since the list is sorted, it will likely find a negative number and look and see if the positive version of that number exists. 

## Linear Search

The first algorithm just searches through every index until either a compliment is found, or until it reaches the end of the list. This method is the most time-consuming.

## Binary Search

The second algorithm uses a binary search. It finds the first number, then looks at the value that lies on the middle index number to see if that's a compliment. If the number is lower than the expected compliment. It then searches the index roughly 3/4 the way through the list. Binary search is faster than linear search as it successively divides the number of possible values in half, looks at the value, and smartly chooses which half to divide.

## Pointer Search

The third algorithm uses pointers at the beginning and end of the list. Unlike the first two algorithms, which look at a specific index and determine if a complement to that index value exists, this algorithm just looks to see if ANY compliment exists within the list at all. Since the beginning and end values in a sorted list are often negative and positive, it sums the values. If the sum of the two values equal zero, then a compliment is found. If the sum of the values is greater than zero, then the end pointer is greater than the beginning pointer, so it decrements the value of the end pointer. Conversely, it increments the value of the beginning pointer if the sum is less than zero.
