def find_permutation(str1, pattern):
  windowStart, matched = 0, 0
  char_frequency = {}

  for char in pattern:
    if char not in char_frequency:
        char_frequency[char] = 0
    char_frequency[char] += 1

  for windowEnd in range(len(str1)):
    right_char = str1[windowEnd]
    if right_char in char_frequency:
        char_frequency[right_char] -= 1
        if char_frequency[right_char] == 0:
            matched += 1
    
    if matched == len(pattern):
        return True
    
    if windowEnd >= len(pattern)-1:
        left_char = str1[windowStart]
        windowStart += 1
        if left_char in char_frequency:
            if char_frequency[left_char] == 0:
                matched -= 1
            char_frequency[left_char] += 1
     
  return False        


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
