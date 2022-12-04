
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

def get_sum_of_elf_calories_(cal_list):
    sum_list = []
    for calorie_list in cal_list:
        sum_list.append(sum(list(map(lambda x: int(x), calorie_list))))
    return sum_list


def main():
    # first half of the puzzle
    file_content = read_file("./day1/input.txt")
    cal_list = parse_file_content(file_content)
    sum_of_elf_calories = get_sum_of_elf_calories_(cal_list)
    max_calorie_count = max(sum_of_elf_calories)
    print(max_calorie_count)

    # second half of the puzzle
    top_three = sorted(sum_of_elf_calories, key=lambda x: int(x), reverse=True)[:3]
    print(sum(top_three))
main()