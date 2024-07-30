board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
rows = [set() for _ in range(9)]
columns = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]


def validSudoku():
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue

            if num in rows[r]:
                return False
            rows[r].add(num)
            if num in columns[c]:
                return False
            columns[c].add(num)

            # Check the 3x3 sub-box
            # if 0 < r <=3 and 0 < c <= 3 -> first box
            if r < 3 and c < 3:
                if num in boxes[0]:
                    return False
                boxes[0].add(num)
            if r < 6 and r >= 3 and c < 3:
                if num in boxes[1]:
                    return False
                boxes[1].add(num)
            if r < 9 and r >= 6 and c < 3:
                if num in boxes[2]:
                    return False
                boxes[2].add(num)
            if r < 3 and c < 6 and c >= 3:
                if num in boxes[3]:
                    return False
                boxes[3].add(num)
            if r < 6 and r >= 3 and c < 6 and c >= 3:
                if num in boxes[4]:
                    return False
                boxes[4].add(num)
            if r < 9 and r >= 6 and c < 6 and c >= 3:
                if num in boxes[5]:
                    return False
                boxes[5].add(num)
            if r < 3 and c < 9 and c >= 6:
                if num in boxes[6]:
                    return False
                boxes[6].add(num)
            if r < 6 and r >= 3 and c < 9 and c >= 6:
                if num in boxes[7]:
                    return False
                boxes[7].add(num)
            if r < 9 and r >= 6 and c < 9 and c >= 6:
                if num in boxes[8]:
                    return False
                boxes[8].add(num)
    return True


print(validSudoku())
print()
