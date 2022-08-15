def length_of_longest_substring(arr, k):
    windowStart = 0
    maxLengthOnes = 0
    maxLength =0

    for windowEnd in range(len(arr)):
        if arr[windowEnd] == 1:
            maxLengthOnes += 1
        if windowEnd - windowStart + 1 - maxLengthOnes > k:
            if arr[windowStart] == 1:
                maxLengthOnes -= 1
            windowStart += 1
        maxLength = max(maxLength , windowEnd - windowStart + 1)
    return maxLength 









def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
