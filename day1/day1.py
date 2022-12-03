
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"file {filename} does not exist")
        return None

def parse_file_content(file_content):
    calorie_lists = []
    sub_calorie_list = []
    for line in file_content:
        if line == '\n':
            calorie_lists.append(sub_calorie_list[:])
            sub_calorie_list.clear()
        else:
            sub_calorie_list.append(line)
    return [list(map(lambda x: x.strip(), calorie_list)) for calorie_list in calorie_lists]

def elf_with_most_calories(cal_list):
    sum_list = []
    for calorie_list in cal_list:
        sum_list.append(sum(list(map(lambda x: int(x), calorie_list))))
    return max(sum_list)


def main():
    file_content = read_file("./day1/input.txt")
    cal_list = parse_file_content(file_content)
    max_calorie_count = elf_with_most_calories(cal_list)
    print(max_calorie_count)

main()