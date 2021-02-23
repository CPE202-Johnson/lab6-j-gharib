import random
import time

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

    
def insertion_sort(listy):
    comparisons = 0
    for i in range(len(listy) - 1):
        sortInd = i + 1
        if listy[sortInd] < listy[i]:
            comparisons += 1
            j = i
            ind2 = sortInd
            while j >= 0:
                comparisons += 1
                if listy[j] > listy[ind2]:
                    temp = listy[ind2]
                    listy[ind2] = listy[j]
                    listy[j] = temp
                ind2 -= 1
                j -= 1
    return comparisons




def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    
    #random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 1000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()
