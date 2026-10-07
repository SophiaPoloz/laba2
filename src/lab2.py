# Лабораторна робота №2. Створення та використання функцій, реалізація рекурсії
# Варіант: 8
# ПІБ: Полоз Софія Юріївна

# Тут має бути Ваш код
import random

# Створення набору даних 20 ел мінімум
genres = ["Фантастика", "Детектив", "Наука", "Історія", "Роман"]
books = [
    {
        "id": i,
        "title": f"Книга_{i}",
        "genre": random.choice(genres),
        "year": random.randint(1900, 2026),
        "pages": random.randint(100, 800)
    }
    for i in range(1, 20)
]

# Розробка набору функцій
def display_book(book):
    """Звичайна функція 1: Виведення інформації про книгу"""
    print(
        f"ID: {book['id']} | Назва: {book['title']} | Жанр: {book['genre']} | Рік: {book['year']} | Сторінок: {book['pages']}")

def get_books_by_genre(data, genre):
    """Звичайна функція 2: Пошук книг за жанром"""
    return [b for b in data if b['genre'] == genre]

def calculate_reading_time(pages, speed_pages_per_hour=30):
    """Функція з параметрами за замовчуванням: Розрахунок часу на читання"""
    return round(pages / speed_pages_per_hour, 2)

def total_pages_in_library(*pages):
    """Функція зі змінною кількістю аргументів: Підрахунок загальної кількості сторінок"""
    return sum(pages)

# Лямбда-функції
is_modern = lambda b: b['year'] >= 2000
get_title = lambda b: b['title'].upper()

#  Реалізація рекурсивної функції
def recursive_quicksort_by_year(arr):
    """Складне алгоритмічне завдання: Швидке сортування (QuickSort) книг за роком видання"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]['year']
    left = [x for x in arr if x['year'] < pivot]
    middle = [x for x in arr if x['year'] == pivot]
    right = [x for x in arr if x['year'] > pivot]
    return recursive_quicksort_by_year(left) + middle + recursive_quicksort_by_year(right)

# Функціональне програмування
def custom_filter_books(data, condition_func):
    """Власна функція вищого порядку: Фільтрація книг за переданою умовою"""
    return [item for item in data if condition_func(item)]

#  Інтерактив
def main_library():
    while True:
        print("\n--- Система Управління Бібліотекою ---")
        print("1. Всі книги")
        print("2. Сучасні книги (від 2000 року - filter)")
        print("3. Назви книг великими літерами (map)")
        print("4. Відсортувати книги за роком (Рекурсія QuickSort)")
        print("5. Підрахувати сторінки обраних книг (*args)")
        print("0. Вихід")

        choice = input("Оберіть дію: ")

        if choice == '0':
            break
        elif choice == '1':
            for b in books: display_book(b)
        elif choice == '2':
            modern_books = list(filter(is_modern, books))
            for b in modern_books: display_book(b)
        elif choice == '3':
            titles = list(map(get_title, books))
            print("Назви:", ", ".join(titles[:10]), "...")
        elif choice == '4':
            sorted_books = recursive_quicksort_by_year(books)
            for b in sorted_books: display_book(b)
        elif choice == '5':
            try:
                ids = list(map(int, input("Введіть ID книг через пробіл: ").split()))
                pages_list = [b['pages'] for b in books if b['id'] in ids]
                total = total_pages_in_library(*pages_list)
                print(f"Загальна кількість сторінок: {total}")
            except ValueError:
                print("Помилка: введіть числа!")
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    main_library()

