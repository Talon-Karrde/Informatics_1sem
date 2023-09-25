def spiral_matrix(n, m):
    ma = [[0] * m for _ in range(n)]   
    top, bottom, left, right = 0, n - 1, 0, m - 1  
    num = 1  

    while top <= bottom and left <= right:
        # верхняя строка
        for i in range(left, right + 1):
            ma[top][i] = num
            num += 1
        top += 1

        # правый столбец
        for i in range(top, bottom + 1):
            ma[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            # нижняя строка
            for i in range(right, left - 1, -1):
                ma[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            # левый столбец
            for i in range(bottom, top - 1, -1):
                ma[i][left] = num
                num += 1
            left += 1

    return ma
n=int(input())
m=int(input())
result_ma = spiral_matrix(n, m)
for row in result_ma:
    print(row)
