def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"file {filename} does not exist")
        return []

def create_section_sets(section_1, section_2):
    section_1_set = set()
    section_2_set = set()
    for i in range(int(section_1[0]), int(section_1[1])+1):
        section_1_set.add(i)
    for j in range(int(section_2[0]), int(section_2[1])+1):
        section_2_set.add(j)
    return section_1_set, section_2_set

def calculate_overlapping_sections(splits: list[str], all_overlaps: bool = False):
    overlapping_sessions_count = 0
    for split in splits:
        elves_groups = split.split("\n")[:-1]
        for sections in elves_groups:
            section_range_1, section_range_2 = sections.split(",")
            section_1, section_2 = section_range_1.split("-"), section_range_2.split("-")
            set_1, set_2 = create_section_sets(section_1, section_2)
            if not all_overlaps:
                if (
                    min(set_1) >= min(set_2) and max(set_1) <= max(set_2) or
                    min(set_2) >= min(set_1) and max(set_2) <= max(set_1) and
                    set_1.intersection(set_2)
                ):
                    overlapping_sessions_count += 1
            else:
                if set_1.intersection(set_2):
                    overlapping_sessions_count += 1

    return overlapping_sessions_count


def main():
    # part 1
    lines = read_file("./day4/real.txt")
    overlap_count = calculate_overlapping_sections(lines)
    print(overlap_count)

    # part 2
    all_overlap_count = calculate_overlapping_sections(lines, True)
    print(all_overlap_count)

    
main()