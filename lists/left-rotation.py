import os

# Complete the rotLeft function below.
def rotLeft(a, d):
    result = a.copy()
    for i in range(len(a)):
        result[i] = a[(i+d)%(len(a))]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()