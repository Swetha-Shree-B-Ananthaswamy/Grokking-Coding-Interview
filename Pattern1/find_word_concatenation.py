def find_word_concatenation(str1, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    wordFrequency = {}
    for word in words:
        if word not in wordFrequency:
            wordFrequency[word] =0
        wordFrequency[word] += 1
    
    wordCount = len(words)
    wordLength = len(words[0])
    resultIndies =[]

    for i in range((len(str1) - wordCount * wordLength)+1):
        wordSeen ={}
        for j in range(0, wordCount):
             
            nextWordIndex = i +j*wordLength
            word = str1[nextWordIndex : nextWordIndex+wordLength]
            if word not in wordFrequency:
                break;
            
            if word not in wordSeen:
                wordSeen[word] = 0
            wordSeen[word] += 1

            if wordSeen[word] > wordFrequency.get(word ,0):
                break
            
            if  j+1 == wordCount:
                resultIndies.append(i)

    return resultIndies


def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()
