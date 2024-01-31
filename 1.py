def compare_files(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        lines_file1 = file1.readlines()
        lines_file2 = file2.readlines()

    different_lines_file1 = [line for line in lines_file1 if line not in lines_file2]
    different_lines_file2 = [line for line in lines_file2 if line not in lines_file1]

    return different_lines_file1, different_lines_file2

file_path1 = 'file1.txt'
file_path2 = 'file2.txt'

result = compare_files(file_path1, file_path2)

different_lines_file1, different_lines_file2 = result

print("Lines that do not match in file 1:")
for line in different_lines_file1:
    print(line.strip())

print("\nLines that do not match in file 2:")
for line in different_lines_file2:
    print(line.strip())
