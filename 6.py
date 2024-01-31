def replace_word_in_file(file_path, target_word, replacement_word):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    updated_content = content.replace(target_word, replacement_word)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

file_path = 'your_file.txt'

target_word = input("Введіть слово для заміни: ")

replacement_word = input("Введіть нове слово: ")

replace_word_in_file(file_path, target_word, replacement_word)

print(f"Слово '{target_word}' було замінено на '{replacement_word}' у файлі {file_path}")
