#Maximum Sum Subarray of Size K (easy)

def find_maximum_sum_of_subarray(k, arr):

    windowSum = 0
    windowStart = 0
    maxSumOfSubarray =0

    for windowEnd in range(len(arr)):

        windowSum += arr[windowEnd]

        if windowEnd >= k - 1:
            maxSumOfSubarray = max(maxSumOfSubarray , windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    
    return maxSumOfSubarray 

def main():
  print("Maximum sum of a subarray of size K: " + str(find_maximum_sum_of_subarray(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(find_maximum_sum_of_subarray(2, [2, 3, 4, 1, 5])))


main()