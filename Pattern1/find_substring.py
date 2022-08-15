def find_substring(str1, pattern):
    windowStart = 0
    matched =0
    subStringStart =0
    minLength = len(str1) + 1
    charFrequency = {}

    for char in pattern:
        if char not in charFrequency:
            charFrequency[char] = 0
        charFrequency[char] += 1
    

    for windowEnd in range(len(str1)):
        rightChar = str1[windowEnd]
        if rightChar in charFrequency:
            charFrequency[rightChar] -= 1
            if charFrequency[rightChar] >= 0:
                matched += 1
        
        while matched == len(pattern):
            if minLength > windowEnd - windowStart + 1:
                minLength = windowEnd - windowStart + 1
                subStringStart = windowStart
            
            left_char = str1[windowStart]
            windowStart += 1
            if left_char in charFrequency:
                if charFrequency[left_char] == 0:
                    matched -= 1
                charFrequency[left_char] += 1
             
    if minLength > len(str1):
        return "";
    else:
        return str1[subStringStart:subStringStart + minLength] 








def main():
  print(find_substring("aabdec", "abc"))
  print(find_substring("aabdec", "abac"))
  print(find_substring("abdbca", "abc"))
  print(find_substring("adcad", "abc"))

main()