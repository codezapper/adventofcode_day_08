HEADER_SIZE = 2


def get_numbers_from_file(filename):
    try:
        with open(filename, "r") as input_file:
            input_lines = input_file.readlines()
            if len(input_lines) < 1:
                return []
            numbers = list(map(int, input_lines[0].split()))
    except FileNotFoundError as error:
        print(f"Cannot open {filename} - aborting")
        return None

    return numbers


def get_and_remove_node(numbers, start_index):
    meta_count = numbers[start_index + 1]
    end_index = HEADER_SIZE + start_index + meta_count
    current_node = numbers[start_index:end_index]

    del numbers[start_index:end_index]

    return current_node


# Normally a parameter to a function should not have an
# empty list as default value, because a list is mutable
# and it may lead to unwanted side effects. In this case
# though, this is what we want and we can use this effect
# to our advantage, to keep track of the metadata numbers
# while processing.
def extract_metadata(numbers, start_index=0, metadata=[]):
    if len(numbers) == 0:
        return []

    children_count = numbers[start_index]

    # This will loop over all the children and recursively
    # go in depth until a node with no children is found
    for i in range(children_count):
        extract_metadata(numbers, start_index + HEADER_SIZE)

    current_node = get_and_remove_node(numbers, start_index)
    metadata.extend(current_node[HEADER_SIZE:])
    return metadata


def main():
    numbers = get_numbers_from_file("input.txt")
    if numbers is not None:
        meta = extract_metadata(numbers)
        print(sum(meta))


if __name__ == "__main__":
    main()
