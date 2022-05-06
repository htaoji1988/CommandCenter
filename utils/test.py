def check(x, y, val, matrix):
    for i in matrix[x]:
        if i == val:
            return False
    for j in range(9):
        if matrix[j][y] == val:
            return False
    area_row = (x // 3) * 3
    area_col = (y // 3) * 3
    for i in range(area_row, area_row + 3):
        for j in range(area_col, area_col + 3):
            if matrix[i][j] == val:
                return False
    return True


def dfs(index, data, matrix):
    if index == len(data):
        return True

    for i in range(1, 10):
        r, c = data[index]
        if check(r, c, i, matrix):
            matrix[r][c] = i
            cache = dfs(index + 1, data, matrix)
            if cache:
                return True
            matrix[r][c] = 0


while True:
    try:
        matrix = []
        for i in range(9):
            r = [int(j) for j in input().split()]
            matrix.append(r)
        get_0 = []  # 为0的单元格
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    get_0.append((i, j))
        dfs(0, get_0, matrix)
        for m in matrix:
            print(' '.join(map(str, m)))
    except:
        break
