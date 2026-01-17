"""
    This program tests three algorithms which do the same thing:
    take a sorted list and determine if there are any cases where
    one value in the list is the complement of another (sum == 0)
    and returns true if that's the case. 

    Filename:       Project2_Algorithm_Analysis_Kurta.py
    Author:         Michael Kurta
    Date:           10/3/2025
    Course:         COMP 1353
    Assignment:     Project 2 - Algorithm Analysis
    Collaborators:  None
    Internet Source:None
"""
LIST_SIZE       = 10000
NUM_ITERATIONS  = 2
BOUNDS_ABS      = 10

import random
import time

def generate_list(size: int, max_bounds: int = BOUNDS_ABS)->list:
  """
  Generates a random list of integer numbers of positive and negative values.
  parameters: 
            size : int
              size of desired list 
            max_bounds :
              maximum absolute value of numbers generated in the list
  returns
      list of random values
  """
  my_list = []

  for i in range(LIST_SIZE):
    my_list.append(random.randint(-BOUNDS_ABS, BOUNDS_ABS))

    while my_list[-1] == 0:  # Loop so we don't ever have 0 as a number in the list

      my_list[-1] = random.randint(-BOUNDS_ABS, BOUNDS_ABS)
  
  return my_list

def generate_worst_list(size: int, max_bounds: int = BOUNDS_ABS)->list:
  """
  Generates a list of random numbers that includes the worst case scenario for a method that determines
  if a list contains both a number and it's negative complement. In this list, everything is positive, which 
  will guarantee that the test will fail and takes the maximum amount of time.
  parameters: 
            size : int
              size of desired list 
            max_bounds :
              maximum absolute value of numbers generated in the list
  returns
      list of random values
  """
  my_list = []

  for i in range(LIST_SIZE):
    my_list.append(random.randint(1, BOUNDS_ABS))
  
  return my_list

def generate_worst_list2(size: int, max_bounds: int = BOUNDS_ABS)->list:
  """
  Generates a list of random numbers that includes the worst case scenario for a method that determines
  if a list contains both a number and it's negative complement. Specifically for algorithm 3, which uses:
  
  "incrementing and / or decrimenting markers and determining which one to change based on their sum. If the
  markers cross eachother without finding a sum equal to zero, the test fails."

  This generator ensures the maximum time to complete this task by generating random negative numbers less than -1
  and then appending a '1' to the end of the list. The trailing marker will keep incrementing while their sum remains
  less than zero.
  parameters: 
            size : int
              size of desired list 
            max_bounds :
              maximum absolute value of numbers generated in the list
  returns
      list of random values
  """
  my_list = []

  for i in range(LIST_SIZE - 1):
    my_list.append(random.randint(-BOUNDS_ABS, -2))
  
  my_list.append(1)
  
  return my_list
  
  

def alg1(some_list: list[int])->bool:
  """
  Algorithm which checks if there exists some value in the list that also has its compliment
  (inverted sign) also within the list.

  It does so by iterating through every element in the list without regard to its value.
  Therefore, this a O(n) operation at worst for each element that is checked, and therefore 
  O(n^2) for checking the entire list

  parameters
    some_list : list

  returns
      bool : True if that some number combo exists in the list
  """
  # Return False if empty list
  if not some_list:
    return False

  for i in range(len(some_list)):   # Loop though outer loop for the indices to compare against
    value = some_list[i]
    for j in range(len(some_list)): # Loop through inner loop to compare i to j
      if some_list[j] == -(value):  # Check if the current value is the complement to the target
        return True
  
  return False

def alg2(some_list: list[int])->bool:
  """
  Algorithm which checks if there exists some value in the list that also has its compliment
  (inverted sign) also within the list.

  It does so by iterating through via binary search method for every comparison.
  Worst case is O(log2(n)), as each new search iteration reduces the search area by two.
  i.e. (n/2 + n/4 + n/8 + n/16...).
  The entire list takes O(nlog2(n)). (Initial operation times n iterations)

  parameters
    some_list : list

  returns
      bool : True if that some number combo exists in the list
  """
  length = len(some_list)
  for i in range(length):
    start = i
    end = length - 1

    # Return False if empty list
    if not some_list:
      return False
    
    # If start > end, the list has failed to find a match
    while start <= end:
      
      # Set the new midpoint to check
      mid = (start + end) // 2

      # Return True if the midpoint is a match
      if some_list[mid] == -some_list[i]:
        return True
      
      # If the midpoint value is lower than the target value
      elif some_list[mid] < -(some_list[i]):
        start = mid + 1   # Set the new lower bounds at 1 + the midpoint

      else:
        end = mid - 1     # If higher, drop the endpoint to one less than the midpoint
  
  return False
    
def alg3(some_list: list[int])->bool:
  """
    Algorithm which checks if there exists some value in the list that also has its compliment
    (inverted sign) also within the list.

    It does so by setting markers at the beginning and the end of the list, and checking their sum.
    If the sum is equal to 0, then a compliment is found.
    Since we know the list is sorted, it can smartly walk its markers and quickly determine if there is a match at all. 
    This algorithm does not bother with individual comparisons like the binary sort: rather, it determines if there is a match 
    of any sort. The process is O(n) for the entire calculation since there must be at max n-1 comparisons. At any one time, only one index moves.
    
    The algorithm will take longer if the division between negative and positive integers is towards the end of the array.
    for example, my_array = [-25, -24, -23, -22, ....., -2, 1] will take the maximum amount of time to execute for the array size.

    parameters
      some_list : list

    returns
        bool : True if that some number combo exists in the list
    """
  i = 0
  j = len(some_list) - 1
  not_found = True
  
  if not some_list:
    return False


  while not_found:
    # If the indeces cross... there is not a match
    if i >= j:
      return False
    
    sum = some_list[i] + some_list[j]

    # If their sum equals zero, we've found a match
    if sum == 0:
      not_found = False
      return True
    
    # If the sum is less than zero, increment the lower index
    elif sum < 0:
      i += 1

    # If the sum is less than zero, decrement the upper index
    else:
      j -= 1
  
  return False

    
def main():

  my_list   = generate_worst_list(LIST_SIZE, BOUNDS_ABS)
  my_list2  = generate_worst_list2(LIST_SIZE, BOUNDS_ABS)

  my_list.sort()
  my_list2.sort()

  # Test 1 #
  start = time.time()
  for i in range(NUM_ITERATIONS):
    alg1(my_list)
  stop = time.time()

  print("Algorithm 1:\t\tAvg time\t\tElapsed time")
  print(f"\t\t{(stop - start) / NUM_ITERATIONS}\t\t{stop - start}")

  # Test 2 #
  start = time.time()
  alg2(my_list)
  stop = time.time()

  print("Algorithm 2:\t\tAvg time\t\tElapsed time")
  print(f"\t\t{(stop - start) / NUM_ITERATIONS}\t\t{stop - start}")

  # Test 3 #
  start = time.time()
  alg3(my_list2)
  stop = time.time()

  print("Algorithm 3:\t\tAvg time\t\tElapsed time")
  print(f"\t\t{(stop - start) / NUM_ITERATIONS}\t\t{stop - start}")



if __name__ == "__main__":

  main ()

