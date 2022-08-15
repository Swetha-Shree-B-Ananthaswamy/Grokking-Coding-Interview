def non_repeat_substring(str1):
    windowStart =0
    maxLength =0
    char_frequency ={}
    for windowEnd in range(len(str1)):
        right_char = str1[windowEnd]
        
        if right_char in char_frequency:
            windowStart = max(windowStart , char_frequency[right_char] + 1)

        char_frequency[right_char] = windowEnd
        maxLength = max(maxLength , windowEnd - windowStart + 1)
    return maxLength

def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()
