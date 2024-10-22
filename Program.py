import string

# Функція для видалення пунктуації та сортування слів
def sort_words(words):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_words = [word.translate(translator) for word in words]
    # Сортування спочатку українських, потім англійських слів
    ukrainian_words = sorted([word for word in cleaned_words if any('а' <= ch <= 'я' or ch == 'ї' or ch == 'є' or ch == 'і' or ch == 'ґ' for ch in word.lower())])
    english_words = sorted([word for word in cleaned_words if all('a' <= ch.lower() <= 'z' for ch in word)])
    return ukrainian_words, english_words

# Функція для зчитування першого речення з файлу
def read_first_sentence(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            # Розбивка на речення по знаку кінця речення (наприклад, крапка)
            sentences = text.split('.')
            if sentences:
                return sentences[0].strip()
            else:
                return ""
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return None

# Функція для виведення інформації
def process_text(filename):
    first_sentence = read_first_sentence(filename)
    if first_sentence:
        print(f"Перше речення: {first_sentence}")

        # Отримання всіх слів з тексту
        words = first_sentence.split()

        # Сортування слів за українськими та англійськими
        ukrainian_words, english_words = sort_words(words)

        # Виведення результатів
        print("\nВідсортовані українські слова:")
        print(ukrainian_words)

        print("\nВідсортовані англійські слова:")
        print(english_words)

        total_words = len(ukrainian_words) + len(english_words)
        print(f"\nЗагальна кількість слів: {total_words}")

# Виклик основної функції
filename = 'textfile.txt'  # Назва вашого текстового файлу
process_text(filename)
