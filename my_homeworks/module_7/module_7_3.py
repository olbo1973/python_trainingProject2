# Домашнее задание по теме "Оператор "with".
# Задача "Найдёт везде":

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:  # Проверить, что файлы открываются в правильной
                    # кодировке
                    text = file.read().lower()  # Считываем и преобразуем в нижний регистр
                    for punct in [',', '.', '=', '!', '?', ';', ':', '-']:  # Убираем пунктуацию
                        text = text.replace(punct, '')
                    all_words[file_name] = text.split()  # Разбиваем текст на слова
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Ошибка при чтении файла {file_name}: {e}")
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_position = {}
        for file_name, words in all_words.items():
            if word in words:
                word_position[file_name] = words.index(word) + 1  # Позиция в 1-индексации
        return word_position

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_counts = {}
        for file_name, words in all_words.items():
            word_counts[file_name] = words.count(word)  # Подсчет вхождений
        return word_counts


# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  ## 4 слова teXT в тексте всего

print()

finder3 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder3.get_all_words())
print(finder3.find('Child'))
print(finder3.count('Child'))

print()

finder4 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder4.get_all_words())
print(finder4.find('if'))
print(finder4.count('if'))

print()

finder5 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder5.get_all_words())
print(finder5.find('captain'))
print(finder5.count('captain'))

### Описание кода:
# 1. **Конструктор `__init__`:**
 # принимает неограниченное количество имен файлов и сохраняет их в атрибут `file_names`.
 # 2. **Метод `get_all_words`:**
 #    - Открывает каждый файл, считывает его содержимое, переводит в нижний регистр.
 #    - Убирает пунктуацию и пробелы.
 #    - Разбивает текст на слова и создает словарь с названием файла как ключом и списком слов как значением.
 # 3. **Метод `find`:**
 # ищет указанное слово в словах всех файлов и возвращает словарь с названиями файлов и позициями первого вхождения слова.
 # 4. **Метод `count`:**
 # подсчитывает количество вхождений указанного слова в каждом файле и возвращает словарь с названиями файлов и
 # количеством вхождений.