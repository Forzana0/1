def count_word_occurrences(file_path, target_word):
    with open(file_path, 'r') as file:
        content = file.read()

    word_count = content.lower().split().count(target_word.lower())

    return word_count

file_path = 'your_file.txt'

target_word = input("Введіть слово для підрахунку: ")

occurrences = count_word_occurrences(file_path, target_word)

print(f"Кількість входжень слова '{target_word}' у файлі: {occurrences}")
