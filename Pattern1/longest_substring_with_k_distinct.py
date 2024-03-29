def longest_substring_with_k_distinct(str1, k):
    windowStart = 0
    maxLength = 0
    char_frequency ={}
    for windowEnd in range(len(str1)):
        right_char = str1[windowEnd] 
        if  right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > k:
            left_char = str1[windowStart]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            windowStart += 1
        
        maxLength = max(maxLength , windowEnd - windowStart +1)

    return maxLength




def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
