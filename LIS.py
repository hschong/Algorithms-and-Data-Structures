'''
Dynamic Programming

Longest Increasing Subsequence(최장 증가 부분 수열)

수열 a에 대하여, 부분수열이란 a에서 몇 개의 원소를 골라서 만들 수 있는 수열을 말한다. 예를 들어, 
수열 a = [1, 4, 2, 8] 이라고 할 때, 수열 a의 부분수열이 될 수 있는 것으로는 
[1], 
[1, 4], [1, 2], [1, 8], 
[1, 4, 2], [1, 4, 8], [1, 2, 8],
[1, 4, 2, 8] ...... 등이 있다.

증가수열이란, 수열의 원소가 갈수록 증가하는 수열을 말한다. 예를 들어, [1, 2, 3], [1, 2, 5], 
[3, 4, 8] 는 증가수열이지만 [1, 4, 2] 는 증가수열이 아니다. 수열 a에 대하여, 증가 부분 수열이란 
a의 부분수열 중에서 증가수열에 해당되는 것을 말한다. 예를 들어, 수열 a = [1, 4, 2, 8] 이라고 
할 때, 수열 a의 증가 부부 수열이 될 수 있는 것으로는 [1], [1, 2, 8], [1, 4, 8] 등이 있다.

수열 a에 대하여, 최장 증가 부분 수열이란 a의 증가 부분 수열 중에서 그 길이가 최대인 것을 말한다. 
예를 들어, 수열 a = [1, 4, 2, 8] 이라고 할 때, 최장 증가 부분 수열의 길이는 3이다.
수열이 주어질 때, 최장 증가 부분 수열의 길이를 구하는 프로그램을 작성하세요.


입력
수열의 원소가 주어진다. 그 길이는 100보다 작거나 같다.

출력
최장 증가 부분 수열의 길이를 출력한다.

입력 예시
1 4 2 3 5

출력 예시
4
'''

import sys


def LIS(numbers):
    '''
    수열이 list로 주어질 때, 최장 증가 부분 수열의 길이를 반환하는 함수를 작성하세요.
    T[i]: i번째 숫자를 오른쪽 끝으로 하는 LIS 의 길이
    T[i] = max(T[j] + 1) if numbers[j] < numbers[i]

    ex)
    2 5 3 4 6 1
    T[0] = 1, [2]
    T[1] = 2, [2, 5]
    T[2] = 2, [2, 3]
    T[3] = 3, [2, 3, 4]
    T[4] = 4, [2, 3, 4, 6]
    T[5] = 1, [1]
    max(T) = 4
    O(N^2)
    '''

    length = len(numbers)
    Table = [0 for i in range(length)]

    # Base case
    Table[0] = 1
    for i in range(1, length):
        Table[i] = 1

        for j in range(0, i):
            if numbers[j] < numbers[i]:
                Table[i] = max(Table[i], Table[j] + 1)

    return max(Table)


def main():
    numbers = [int(data) for data in input().split()]
    print(LIS(numbers))


if __name__ == "__main__":
    main()
