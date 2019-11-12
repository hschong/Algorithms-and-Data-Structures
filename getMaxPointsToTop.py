'''
Dynamic Programming

계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 
가는 게임이다. <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 
계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.

                          --------
                          |20 도착
                      ----
                      |10 
                  ----
                  |25 
              ----
              |15 
          ----
          |20 
      ----
      |10 
--------------------------------
 시작

계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 
밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다. 
연속된 세 개의 계단을 모두 밟아서는 안된다. 단, 시작점은 계단에 
포함되지 않는다. 마지막 도착 계단은 반드시 밟아야 한다. 따라서 첫 번째 
계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 
하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 
두 번째, 세번째 계단을 연속해서 모두 밟을 수는 없다.

입력
제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 
계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 
10,000이하의 자연수이다.

출력
첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최대값을 출력한다.

입력 예시
10 20 15 25 10 20

출력 예시
75

'''

import sys


def getMaxPointsToTop(pointList):
    '''
    각 계단에 쓰여있는 점수가 list로 주어질 때, 이 게임에서 얻을 수 
    있는 총 점수의 최댓값을 반환하는 함수를 작성하세요.

    T(i) : i번째 계단을 마지막으로 밟는 총 점수의 최대 값
    T(i) = max( T(i-2) + data(i), T(i-3) + data(i-1) + data(i) )
    '''

    stairs = len(pointList)
    Table = [0 for i in range(stairs)]

    if stairs == 0:
        return 0
    elif stairs == 1:
        return pointList[0]
    elif stairs == 2:
        return pointList[0] + pointList[1]
    elif stairs == 3:
        return max(pointList[0]+pointList[2], pointList[1] + pointList[2])

    Table[0] = pointList[0]
    Table[1] = pointList[0] + pointList[1]
    Table[2] = max(pointList[0] + pointList[2], pointList[1] + pointList[2])

    for i in range(3, stairs):
        Table[i] = max(Table[i-2] + pointList[i],
                       Table[i-3] + pointList[i-1] + pointList[i])

    return Table[stairs-1]


def main():

    pointList = [int(x) for x in input().split()]
    print(getMaxPointsToTop(pointList))


if __name__ == "__main__":
    main()
