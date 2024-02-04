1. Описание:

Проверяемый класс BooksCollector находится в main.py
Для тестов используются методы класса TestBooksCollector, файл tests.py
В conftest.py находится фикстура, необходимая для корректной работы тестов


2. Запуск тестов:

Запустить тесты можно с помощью команды: pytest tests.py
Более подробный вывод результата тестов: pytest -v tests.py


3. Описание тестов из tests.py:

# класс, в котором хранятся методы для тестирования
class TestBooksCollector
# тестируем метод init_
    test_init_genre # проверяем корректную работу одного из параметров 
# тестируем метод add_new_book
    test_add_new_book_add_two_books # проверяем возможность добавления книги в books_genre
    test_add_new_book_add_same_books # проверяем невозможность добавления книг с одинаковым названием
    test_add_new_book_with_40_symbol # проверяем невозможность добавления книги с названием, в котором больше 40 символов
# тестируем метод set_book_genre
    test_set_book_genre_add_correct_genre # устанавливаем жанр книге, которая есть в books_genre
    test_set_book_genre_add_non_exist_genre # проверяем невозможность устанавливить жанр книге, которой нет в books_genre
# тестируем метод get_book_genre
    test_get_book_genre_get_correct_genre # получаем жанр по книге, которая есть в books_genre. Используем параметризацию.
    test_get_book_genre_get_non_exist_genre # проверяем невозможность получения жанра по книге, которой нет в books_genre
# тестируем метод get_books_with_specific_genre
    test_get_books_with_specific_genre_get_correct_book # получаем название книги по жанру, который есть в genre
    test_get_books_with_specific_genre_get_non_exist_book # проверяем невозможность получения названия книги по жанру, которого нет в books_genre
# тестируем метод get_books_genre
    test_get_books_genre # проверяем корректность получения словаря books_genre
# тестируем метод get_books_for_children
    test_get_books_for_children # проверяем корректность получения книг с возрастным ограничением
# тестируем метод add_book_in_favorites
    test_add_book_in_favorites # проверяем корректность добавляения книги в избранное
# тестируем метод delete_book_from_favorites
    test_delete_book_from_favorites # проверяем корректность удаления книги из избранного
# тестируем метод get_list_of_favorites_books
    test_get_list_of_favorites_books # проверяем корректность получения списка favorites