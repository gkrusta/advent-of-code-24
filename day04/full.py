word = "MAS"

DIR = [
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]


def find_word(grid, row, col, x, y):
    for i in range(len(word)):
        posx, posy = row + i * x, col + i * y
        if posx < 0 or posx >= len(grid) or posy < 0 or posy >= len(grid[0]) or grid[posx][posy] != word[i]:
            return False
    return True


def main():
    file = open("input.txt", "r")
    grid = [line.strip() for line in file.readlines()]
    print("GRID:", grid)
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    print("rows:", rows)
    print("cols:", cols)
    for i in range(rows):
        for j in range(cols):
            for x, y in DIR:
                if find_word(grid, i, j, x, y):
                    count +=1
    print("\ncount:", count)


main()