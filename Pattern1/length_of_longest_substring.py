def length_of_longest_substring(str1, k):
    windowStart =0
    frequency_map = {}
    max_repeat_char_length =0
    maxLength =0
    for windowEnd in range(len(str1)):
        right_char = str1[windowEnd]
        
        if right_char not in frequency_map:
            frequency_map[right_char] =0
        frequency_map[right_char] += 1

        max_repeat_char_length = max(max_repeat_char_length , frequency_map[right_char])

        if windowEnd - windowStart + 1 - max_repeat_char_length > k:
            left_char = str1[windowStart]
            frequency_map[left_char] -= 1
            windowStart += 1

        maxLength = max(maxLength , windowEnd - windowStart + 1)
    
    return maxLength


def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()