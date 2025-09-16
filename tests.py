import pytest
from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Хоббит Нежданное приключение')
        collector.add_new_book('Гарри Поттер')
        assert collector.get_books_genre() == {'Хоббит Нежданное приключение': '',
                                               'Гарри Поттер': ''}


    def test_add_new_book_invalid_name_too_long(self, collector):
        collector.add_new_book('ХоббитХоббитХоббитХоббитХоббитХоббитХоббитХоббит')
        assert collector.get_book_genre('ХоббитХоббитХоббитХоббитХоббитХоббитХоббитХоббит') is None


    def test_add_new_book_already_added_book(self, collector):
        collector.add_new_book('Хоббит Нежданное приключение')
        collector.add_new_book('Хоббит Нежданное приключение')
        assert collector.get_books_genre() == {'Хоббит Нежданное приключение': ''}


    @pytest.mark.parametrize('name', ['На север вдоль рядов кукурузы',
                                      'Ниро Вульф и Арчи Гудвин',
                                      'Оно'])
    def test_add_new_book_name_in_the_range(self, name, collector):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()


    def test_set_book_genre_to_existing_book(self, collector):
        collector.add_new_book('Хоббит Нежданное приключение')
        collector.set_book_genre('Хоббит Нежданное приключение', 'Фантастика')
        assert collector.get_books_genre() == {'Хоббит Нежданное приключение': 'Фантастика'}


    def test_set_book_genre_to_not_existing_book(self, collector):
        collector.set_book_genre('Хоббит Нежданное приключение', 'Фантастика')
        assert collector.get_books_genre() == {}


    def test_set_book_genre_to_not_existing_genre(self, collector):
        collector.add_new_book('Хоббит Нежданное приключение')
        collector.set_book_genre('Хоббит Нежданное приключение', 'Науч-поп')
        assert collector.get_books_genre() == {'Хоббит Нежданное приключение': ''}


    def test_get_books_for_children(self, collector):
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_books_for_children() == ['Хоббит']


    @pytest.mark.parametrize('name, genre', [('Хоббит Нежданное приключение', 'Ужасы'),
                                             ('Гарри Поттер', 'Комедии')])
    def test_get_book_genre_by_name(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre


    @pytest.mark.parametrize('name, genre', [('Хоббит Нежданное приключение', 'Ужасы'),
                                             ('Гарри Поттер', 'Комедии')])
    def test_get_books_with_specific_genre(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]


    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Хоббит Нежданное приключение')
        collector.add_book_in_favorites('Хоббит Нежданное приключение')
        assert 'Хоббит Нежданное приключение' in collector.get_list_of_favorites_books()


    def test_add_book_in_favorites_no_duplicates(self, collector):
        collector.add_new_book("Хоббит Нежданное приключение")
        collector.add_book_in_favorites("Хоббит Нежданное приключение")
        collector.add_book_in_favorites("Хоббит Нежданное приключение")
        assert collector.get_list_of_favorites_books().count("Хоббит Нежданное приключение") == 1


    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Хоббит Нежданное приключение')
        collector.add_book_in_favorites("Хоббит Нежданное приключение")
        collector.delete_book_from_favorites("Хоббит Нежданное приключение")
        assert 'Хоббит Нежданное приключение' not in collector.get_list_of_favorites_books()

    
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Хоббит Нежданное приключение')
        collector.add_book_in_favorites("Хоббит Нежданное приключение")
        assert collector.get_list_of_favorites_books() == ['Хоббит Нежданное приключение']