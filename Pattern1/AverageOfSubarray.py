
#Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.

def find_averages_of_subarrays(k , arr):
    results =[]

    for i in range(len(arr) - k +1):

        _sum = 0.0
        for j in range(i, k + i):
            _sum += arr[j]
        results.append(_sum/k)

    return results


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))

main()
