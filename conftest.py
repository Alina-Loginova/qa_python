import pytest
from main import BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.books_genre = {'Маша и медведи': 'Мультфильмы',
                             'Изгоняющий дьявола': 'Ужасы',
                             'Оно': 'Ужасы',
                             'Вместе с верой': 'Мелодрама',
                             'Интерстеллар': ''}
    collector.favorites = ['Маша и медведи', 'Изгоняющий дьявола', 'Вместе с верой', 'Интерстеллар']
    return collector

