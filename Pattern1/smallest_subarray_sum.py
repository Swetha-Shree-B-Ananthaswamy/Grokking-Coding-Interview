import math

def smallest_subarray_sum(s, arr):
    windowStart , windowSum =0,0
    minLen = math.inf
    for windowEnd in range(0, len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= s:
            minLen = min(minLen , windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1
 
    if minLen == math.inf:
        return 0 
    else:
        return minLen





def main():
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


main()
