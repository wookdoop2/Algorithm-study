# level 2
def solution(arr1, arr2):
    answer = []
    ans = []
    num = 0

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[i])):
                num += arr1[i][k] * arr2[k][j]
            ans.append(num)
            num = 0
        answer.append(ans)
        ans = []

    return answer
