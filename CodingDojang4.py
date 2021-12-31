# 2차원 리스트의 가로 세로 입력
# 그 다음에 리스트 요소로 들어갈 문자가 입력
# * 지뢰, . 지뢰가 이닐때 > .에다가 인접(8방향) 지뢰 개수 출력

# 입력 부분
row, col = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

# 처리
# 기준으로
# -1 -1 / 0 -1 / 0 +1
# 0 -1 / 0 0 / 0 1
# +1 -1 / +1 0 / +1 +1

# 0 0 / 0 1 / 0 2
# 1 0 / 1 1 / 1 2
# 2 0 / 2 1 / 2 2

check_list = [[-1, -1], [0, -1], [0, 1],
              [0, -1], [0, 0], [0, 1],
              [1, -1], [1, 0], [1, 1], ]

for row_index, row in enumerate(matrix):
    for col_index, col in enumerate(row):
        if col == '*':
            continue
        else:
            # 순회
            # index가 0 이상 < 범위 < row_index, col_index 이하
            print("row_index : {}, col_index : {}".format(row_index, col_index))
            for row_checknum, col_checknum in check_list:
                row_serach = row_index + row_checknum
                col_serach = col_index + col_checknum

                if (0 <= row_serach < len(check_list)
                        and 0 <= col_serach <= len(check_list[row_index])):
                    print(row_serach, col_serach)
            pass

# 출력부분