from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 8
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
# print(data)
print(header_line)

def isVisible(forest, tree):
    print(f'val = {forest[tree[0]][tree[1]]} for {tree}')
    visible = True
    # check from left
    for p in range( 0, tree[1]):
        if forest[tree[0]][p] >= forest[tree[0]][tree[1]]:
            visible = False
            print(f'{forest[tree[0]][p]} blocks {forest[tree[0]][tree[1]]}')
    if visible:
        return visible
    visible = True
    # check from right
    for p in reversed(range( tree[1] +1, len(forest[0]))):
        print((tree[0],p))
        if forest[tree[0]][p] >= forest[tree[0]][tree[1]]:
            visible = False
            print(f'{forest[tree[0]][p]} blocks {forest[tree[0]][tree[1]]}')
    if visible:
        return visible
    visible = True
    # check from top
    for p in range( 0, tree[0]):
        if forest[p][tree[1]] >= forest[tree[0]][tree[1]]:
            visible = False
            print(f'{forest[p][tree[1]]} blocks {forest[tree[0]][tree[1]]}')
    if visible:
        return visible
    visible = True
    # check from bottom
    for p in reversed(range( tree[0] +1, len(forest))):
        if forest[p][tree[1]] >= forest[tree[0]][tree[1]]:
            visible = False
            print(f'{forest[p][tree[1]]} blocks {forest[tree[0]][tree[1]]}')
    if visible:
        return visible

def solve_part1():
    print(header_line)
    print(f'solution part 1')
    forest = []
    # solution code

    for line in data.splitlines():
        print(line)
    #     create forest matrix
        forest.append(list(line))
    print(forest)

    visible = len(forest)*2 + (len(forest[0])-2)*2
    print(isVisible(forest,(2,1) ))
    for r in range(1, len(forest)-1):
        for c in range(1, len(forest[0])-1):
            visible += 1 if isVisible(forest, (r, c)) else 0

    print( visible)


    print(header_line)

def viewingDistance(forest, tree):
    print(f'val = {forest[tree[0]][tree[1]]} for {tree}{tree[0]}')
    right = 0
    # check to right
    for p in range(tree[1]+1, len(forest[0])):
        print(f'tree{forest[tree [0]][p]} ({(tree[0],p)}')

        right += 1
        if forest[tree[0]][p] >= forest[tree[0]][tree[1]]:
            break
    print(right)
    left = 0
    # check to left
    for p in reversed(range(0, tree[1])):
        print(f'tree{forest[tree [0]][p]} ({(tree[0],p)}')
        left += 1
        if forest[tree[0]][p] >= forest[tree[0]][tree[1]]:
            break
    print(left)
    bottom = 0
    # check to bottom
    for p in range( tree[0]+1, len(forest)):
        print(f'tree:{forest[p][tree[1]]} ({(p, tree[1])}')
        bottom += 1
        if forest[p][tree[1]] >= forest[tree[0]][tree[1]]:
            break
    print(bottom)
    top = 0
    # check to top
    for p in reversed(range( 0, tree[0])):
        print(f'tree:{forest[p][tree[1]]} ({(p, tree[1])}')
        top += 1
        if forest[p][tree[1]] >= forest[tree[0]][tree[1]]:
            break
    print(top)
    score = top * right * bottom * left
    if top + bottom >= 98:
        print(f'top, bottom, left, right:{(top, bottom, left, right)}')
        print('top bottom')
        print(f'val = {forest[tree[0]][tree[1]]} for {tree}')
        print(score)
    if left + right >= 98:
        print('left right')
        print(f'val = {forest[tree[0]][tree[1]]} for {tree}')
        print(score)
    return score
def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code
    forest = []

    for line in data.splitlines():
        # print(line)
    #     create forest matrix
        forest.append(list(line))
    print(forest)

    # visible = len(forest)*2 + (len(forest[0])-2)*2
    scenicScore = []
    # print(viewingDistance(forest,(1,3) ))
    max_score = 0
    for r in range(0, len(forest)):
        for c in range(0, len(forest[0])):
            # print(viewingDistance(forest, (r, c)))
            score = viewingDistance(forest, (r, c))
            max_score = score if score >= max_score else max_score
            scenicScore.append(score)

    # print(scenicScore)
    for p in reversed(range(0, 3)):
        print(f'p={p}')
    print(max_score)
    print(max(scenicScore))
    print(header_line)


if __name__ == '__main__':
    # solve_part1()
    solve_part2()
