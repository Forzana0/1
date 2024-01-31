def remove_last_line(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    if lines:
        lines = lines[:-1]

    with open(output_file_path, 'w') as output_file:
        output_file.writelines(lines)

input_file_path = 'input.txt'

output_file_path = 'output_without_last_line.txt'

remove_last_line(input_file_path, output_file_path)

print("Last line removed. Result saved to", output_file_path)
