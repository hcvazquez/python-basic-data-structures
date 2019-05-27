'''
 return an integer representing the minimum number of swaps to sort the array.
'''

import os


def minimumSwaps(arr):
    def swap(i, j, arr):
        aux = arr[i]
        arr[i] = arr[j]
        arr[j] = aux

    count = 0
    dic_index = {arr[index]: index for index in range(len(arr))}

    for i in range(len(arr)):
        if arr[i] != i + 1:
            ind = dic_index[i + 1]
            swap(i, ind, arr)
            dic_index[i + 1] = i
            dic_index[arr[ind]] = ind
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
