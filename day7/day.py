from data import get_data_from_file, get_data_from_file_as_int_list, header_line

DAY = 7
data = get_data_from_file(f"day{DAY}.input")
print(f'transformed data for solution')
# print(data)
print(header_line)


def print_dir(dir):
    print(f'{dir["dirname"]}, {dir["size"]}, {dir["subdir"]}')
    for subdir in dir['subdir']:
        # print(f'{subdir["dirname"]}, {subdir["size"]}, {subdir["subdir"]}')
        print_dir(subdir)


def add_subdir_size(dir):
    if dir["subdir"] == []:
        return dir["size"]
    for subdir in dir['subdir']:
        dir["size"] += add_subdir_size(subdir)
    return dir["size"]


acc = 0

def sum_total_le_100000(dir):

    if dir["subdir"] == []:
        return dir['size'] if dir['size'] <= 100000 else 0
    acc = 0
    for subdir in dir['subdir']:
        acc += sum_total_le_100000(subdir)
    print(acc)
    return acc + dir['size'] if dir['size'] <= 100000 else acc



def solve_part1():
    print(header_line)
    print(f'solution part 1')
    cwd = {'dirname': '/', 'size': 0, 'subdir': [], 'parent': None}
    root = cwd
    # solution code
    for line in data.splitlines():
        # Read command
        # if CD set cur directory to next token
        if line[0] == '$':
            print(f'command: {line[2:]}')
            cmd = line[2:].split(' ')
            if cmd[0] == 'cd':
                print(f'change dir to {cmd[1]}')
                if cmd[1] == '..':
                    cwd = cwd['parent']
                else:
                    #     find dir in subdir list
                    for dir in cwd['subdir']:
                        if dir['dirname'] == cmd[1]:
                            cwd = dir
            if cmd[0] == 'ls':
                print('dir listing')
        # if starts with number add values to cwd
        elif line[0].isdigit():
            filesize = int(line.split(' ')[0])
            print(f'Line is a file size {filesize}')

            cwd['size'] += filesize
            print(cwd)
        elif line.split()[0] == 'dir':
            cwd['subdir'].append({'dirname': line.split()[1], 'size': 0, 'subdir': [], 'parent': cwd})
    add_subdir_size(root)
    print_dir(root)
    print(sum_total_le_100000(root))
    print(header_line)


def get_delete_candidates(dir, required):

    if dir["subdir"] == []:
        return dir['size'] if dir['size'] >= required else None
    candidates = []
    for subdir in dir['subdir']:
        val = get_delete_candidates(subdir, required)
        if val:
            if type(val) is list:
                candidates.extend(val)
            else:
                candidates.append(val)
    if dir['size'] >= required:
        candidates.append(dir['size'])
    return candidates

def solve_part2():
    print(header_line)
    print(f'solution part 2')
    # solution code
    total_space = 70000000
    cwd = {'dirname': '/', 'size': 0, 'subdir': [], 'parent': None}
    root = cwd
    # solution code
    for line in data.splitlines():
        # Read command
        # if CD set cur directory to next token
        if line[0] == '$':
            print(f'command: {line[2:]}')
            cmd = line[2:].split(' ')
            if cmd[0] == 'cd':
                print(f'change dir to {cmd[1]}')
                if cmd[1] == '..':
                    cwd = cwd['parent']
                else:
                    #     find dir in subdir list
                    for dir in cwd['subdir']:
                        if dir['dirname'] == cmd[1]:
                            cwd = dir
            if cmd[0] == 'ls':
                print('dir listing')
        # if starts with number add values to cwd
        elif line[0].isdigit():
            filesize = int(line.split(' ')[0])
            print(f'Line is a file size {filesize}')

            cwd['size'] += filesize
            print(cwd)
        elif line.split()[0] == 'dir':
            cwd['subdir'].append({'dirname': line.split()[1], 'size': 0, 'subdir': [], 'parent': cwd})
    add_subdir_size(root)
    print_dir(root)
    print(f'root contains {root["size"]} which leaves {30000000-(total_space- root["size"])}')
    print(min(get_delete_candidates(root,30000000-(total_space- root["size"]))))
    print(header_line)


if __name__ == '__main__':
    solve_part1()
    solve_part2()
