
def find_string_anagrams(str1, pattern):
    windowStart , matched =0,0
    charFrequency = {}

    for char in pattern:
        if char not in charFrequency:
            charFrequency[char] =0
        charFrequency[char] += 1

    result_indices = []    
    for windowEnd in range(len(str1)):
        right_char = str1[windowEnd]
        if right_char in charFrequency:
            charFrequency[right_char] -=1
            if charFrequency[right_char] == 0:
                matched += 1
        
        if matched == len(pattern):
            result_indices.append(windowStart)
        
        if windowEnd >= len(pattern)-1:
            left_char = str1[windowStart]
            windowStart += 1
            if left_char in charFrequency:
                if charFrequency[left_char] == 0:
                    matched -= 1
                charFrequency[left_char] += 1
    
    return result_indices






def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))


main()