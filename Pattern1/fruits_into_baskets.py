def fruits_into_baskets(fruits):
    windowStart =0
    maxLength = 0
    fruit_Frequency ={}
    for windowEnd in range(len(fruits)):
        rightFruit = fruits[windowEnd]
        if rightFruit not in fruit_Frequency:
            fruit_Frequency[rightFruit] = 0
        fruit_Frequency[rightFruit] += 1

        while len(fruit_Frequency) > 2:
            leftFruit = fruits[windowStart]
            fruit_Frequency[leftFruit] -= 1
            if fruit_Frequency[leftFruit] == 0:
                del fruit_Frequency[leftFruit]
            windowStart += 1

        maxLength = max(maxLength , windowEnd - windowStart + 1)

    return maxLength



def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()