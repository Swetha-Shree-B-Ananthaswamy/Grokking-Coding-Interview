
#Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.

def find_averages_of_subarrays(k ,arr):
    results =[]

    windowSum =0.0
    windowStart =0

    for windowEnd in range(len(arr)):

        windowSum += arr[windowEnd]

        if windowEnd >= k:
            results.append(windowSum / k)
            windowSum -= arr[windowStart]
            windowStart += 1
    
    return results

def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()