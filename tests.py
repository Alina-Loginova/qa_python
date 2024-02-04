import pytest

from main import BooksCollector
class TestBooksCollector:

    def test_init_genre(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2
    def test_add_new_book_add_same_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1
    def test_add_new_book_with_40_symbol(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби; Иванов А.И.')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_add_correct_genre(self, collector):
        collector.set_book_genre('Интерстеллар', 'Фантастика')
        assert collector.books_genre['Интерстеллар'] == 'Фантастика'
    def test_set_book_genre_add_non_exist_genre(self, collector):
        collector.set_book_genre('Интерстеллар', 'Драма')
        assert collector.books_genre['Интерстеллар'] != 'Драма'

    @pytest.mark.parametrize('book_name', ['Маша и медведи', 'Изгоняющий дьявола', 'Оно', 'Вместе с верой'])
    def test_get_book_genre_get_correct_genre(self, collector, book_name):
        assert collector.get_book_genre(book_name) == collector.books_genre[book_name]
    def test_get_book_genre_get_non_exist_genre(self, collector):
        assert collector.get_book_genre('Джон Уик') == None

    def test_get_books_with_specific_genre_get_correct_book(self, collector):
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2
    def test_get_books_with_specific_genre_get_non_exist_book(self, collector):
        assert collector.get_books_with_specific_genre('Драма') == []

    def test_get_books_genre(self, collector):
        assert len(collector.get_books_genre()) == len(collector.books_genre)

    def test_get_books_for_children(self, collector):
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites(self, collector):
        collector.add_book_in_favorites('Оно')
        assert 'Оно' in collector.favorites

    def test_delete_book_from_favorites(self, collector):
        collector.delete_book_from_favorites('Маша и медведи')
        assert 'Оно' not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        assert len(collector.get_list_of_favorites_books()) == 4
