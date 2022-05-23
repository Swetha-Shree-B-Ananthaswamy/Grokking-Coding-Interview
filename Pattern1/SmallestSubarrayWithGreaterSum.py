#Smallest Subarray With a Greater Sum 

import math

def smallest_subarray_sum(s, arr):
    
    windowStart = 0
    windowSum = 0
    min_length = math.inf

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        while windowSum >= s:

            min_length = min(min_length , windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1

    if min_length == math.inf:
        return 0

    return min_length

def main():
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


main()
