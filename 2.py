def analyze_text(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    char_count = len(content)

    line_count = content.count('\n') + 1 

    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in content if char in vowels)

    consonant_count = char_count - vowel_count

    digit_count = sum(1 for char in content if char.isdigit())

    return char_count, line_count, vowel_count, consonant_count, digit_count

def write_statistics(output_file_path, statistics):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("Statistics:\n")
        output_file.write(f"Character count: {statistics[0]}\n")
        output_file.write(f"Line count: {statistics[1]}\n")
        output_file.write(f"Vowel count: {statistics[2]}\n")
        output_file.write(f"Consonant count: {statistics[3]}\n")
        output_file.write(f"Digit count: {statistics[4]}\n")

input_file_path = 'input.txt'

output_file_path = 'output_statistics.txt'

statistics_result = analyze_text(input_file_path)
write_statistics(output_file_path, statistics_result)

print("Statistics have been written to", output_file_path)
