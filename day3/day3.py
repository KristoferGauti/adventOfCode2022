import string

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"file {filename} does not exist")
        return []

def find_the_duplicate_item_in_the_rucksack(rucksack):
    dulplicated_rucksack_items = []
    for compartment in rucksack:
        compartment_index = len(compartment) // 2
        compartment_one = compartment[slice(0, compartment_index)]
        compartment_two = compartment[slice(compartment_index, len(compartment))]
        for character in compartment_one:
            if compartment_two.find(character) != -1:
                dulplicated_rucksack_items.append(character)
                break

    return dulplicated_rucksack_items

def pop_the_longest_rucksack(rucksacks):
    longest_rucksack = ""
    for rucksack in rucksacks:
        if len(rucksack) > len(longest_rucksack):
            longest_rucksack = rucksack
    rucksacks.remove(longest_rucksack)
    return longest_rucksack


def main():
    # Part 1
    alphabet_upper_lower = string.ascii_lowercase + string.ascii_lowercase.upper()
    lines = read_file("./day3/real.txt")

    duplicated_rucksack_items = find_the_duplicate_item_in_the_rucksack(lines)
    if duplicated_rucksack_items:
        sum_of_alphabetical_character_number = 0
        for item in duplicated_rucksack_items:
            alphabetical_character_number = alphabet_upper_lower.index(item) + 1
            sum_of_alphabetical_character_number += alphabetical_character_number
        print(sum_of_alphabetical_character_number)

    # Part 2
    three_rucksacks = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    the_badges = []
    for three_rucksack in three_rucksacks:
        longest_rucksack = pop_the_longest_rucksack(three_rucksack)
        for char in longest_rucksack:
            if char in three_rucksack[0] and char in three_rucksack[1]:
                the_badges.append(char)
                break
    
    sum_of_the_badges = 0
    for badge in the_badges:
        sum_of_the_badges += alphabet_upper_lower.index(badge) + 1
    print(sum_of_the_badges)

main()