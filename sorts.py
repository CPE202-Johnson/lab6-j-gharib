import random
import time

#[] -> int
#Perform a selection sort on a list and return how many comparisons were made
def selection_sort(listy):
    comparisons = 0
    ind = -1
    for i in range(len(listy)):
        j = i + 1
        minVal = listy[i]
        while j < len(listy):
            comparisons += 1
            if listy[j] < minVal:
                ind = j
                minVal = listy[j]
            j += 1
        if minVal < listy[i]:
            listy[ind] = listy[i]
            listy[i] = minVal
    return comparisons

#[] -> int
#Perform an insertion sort on a list and return how many comparisons were made
def insertion_sort(listy):
    comparisons = 0
    for i in range(len(listy) - 1):
        sortInd = i + 1
        sortVal = listy[sortInd]
        j = i
        while(sortVal < listy[j]) and (j >= 0):
            comparisons += 1
            listy[sortInd] = listy[j]
            listy[j] = sortVal
            j -= 1
            sortInd -= 1
            sortVal = listy[sortInd]
    if comparisons == 0:
        comparisons = len(listy) - 1
    return comparisons




def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    
    random.seed(1234) 
    insertion_sort([6, 5, 4, 3, 2, 1])
    # Generate 5000 random numbers from 0 to 999,999
    totalComps = 0
    start_time = time.time() 
    randoms = random.sample(range(1000000), 32000)
    #totalComps += insertion_sort(randoms)
    totalComps += selection_sort(randoms)
    stop_time = time.time()
    print("Time: " + str("{0:0.3f}".format((stop_time - start_time))) + " seconds")


if __name__ == '__main__': 
    main()
