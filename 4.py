def find_longest_line_length(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    longest_line_length = max(len(line) for line in lines)

    return longest_line_length

file_path = 'your_file.txt'

longest_line_length = find_longest_line_length(file_path)

print(f"The length of the longest line in the file is: {longest_line_length}")
