
header_line = '--------------------'
def get_data_from_file(filename):
    with open(filename, "r") as f:
        data = f.read().rstrip()
    print(header_line)
    print(f"reading from file {filename}")
    # print(data)
    # print(header_line)
    return data


def get_data_from_file_as_int_list(filename):
    data = get_data_from_file(filename)
    data = [int(x) for x in data.split(',')]
    return data



