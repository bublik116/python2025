from abc import ABC, abstractmethod
from typing import List, Optional

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    
    def __str__(self):
        status = "Доступна" if self.available else "На руках"
        return f"'{self.title}' - {self.author} (ISBN: {self.isbn}) [{status}]"


class Library:
    def __init__(self):
        self.books: List[Book] = []
    
    def add_book(self, book: Book) -> None:
        """Добавляет новую книгу в библиотеку"""
        self.books.append(book)
        print(f"Книга добавлена в библиотеку: {book.title}")
    
    def remove_book(self, book: Book) -> None:
        """Удаляет книгу из библиотеки"""
        if book in self.books:
            self.books.remove(book)
            print(f"Книга удалена из библиотеки: {book.title}")
        else:
            print(f"Ошибка: книги '{book.title}' нет в библиотеке")
    
    def find_book_by_title(self, title: str) -> Optional[Book]:
        """Ищет книгу по названию (регистронезависимо)"""
        title_lower = title.lower()
        for book in self.books:
            if book.title.lower() == title_lower:
                return book
        return None
    
    def list_available_books(self) -> None:
        """Выводит список всех доступных книг"""
        available_books = [book for book in self.books if book.available]
        if not available_books:
            print("В библиотеке нет доступных книг")
            return
        
        print("Доступные книги в библиотеке:")
        for i, book in enumerate(available_books, 1):
            print(f"{i}. {book}")


class LibraryUser(ABC):
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id
        self.borrowed_books: List[Book] = []
    
    @abstractmethod
    def borrow_book(self, book: Book) -> None:
        pass
    
    @abstractmethod
    def return_book(self, book: Book) -> None:
        pass
    
    def list_borrowed_books(self) -> None:
        if not self.borrowed_books:
            print(f"{self.name} не имеет взятых книг")
        else:
            print(f"{self.name} имеет следующие книги:")
            for i, book in enumerate(self.borrowed_books, 1):
                print(f"{i}. {book}")


class Student(LibraryUser):
    MAX_BOOKS = 3

    def borrow_book(self, book: Book) -> None:
        if not book.available:
            print(f"Ошибка: книга '{book.title}' уже взята другим пользователем")
            return
        
        if len(self.borrowed_books) >= self.MAX_BOOKS:
            print(f"Ошибка: {self.name} уже имеет максимальное количество книг ({self.MAX_BOOKS})")
        else:
            self.borrowed_books.append(book)
            book.available = False
            print(f"Студент {self.name} взял книгу: '{book.title}'")

    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"Студент {self.name} вернул книгу: '{book.title}'")
        else:
            print(f"Ошибка: {self.name} не брал книгу '{book.title}'")


class Teacher(LibraryUser):
    MAX_BOOKS = 5

    def borrow_book(self, book: Book) -> None:
        if not book.available:
            print(f"Ошибка: книга '{book.title}' уже взята другим пользователем")
            return
        
        if len(self.borrowed_books) >= self.MAX_BOOKS:
            print(f"Ошибка: {self.name} уже имеет максимальное количество книг ({self.MAX_BOOKS})")
        else:
            self.borrowed_books.append(book)
            book.available = False
            print(f"Преподаватель {self.name} взял книгу: '{book.title}'")

    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"Преподаватель {self.name} вернул книгу: '{book.title}'")
        else:
            print(f"Ошибка: {self.name} не брал книгу '{book.title}'")


# Пример использования
def main():
    # Создаем библиотеку
    library = Library()

    # Добавляем книги в библиотеку
    book1 = Book("Война и мир", "Лев Толстой", "978-5-389-06256-6")
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", "978-5-17-067678-0")
    book3 = Book("Философия Python", "Лучано Рамальо", "978-5-496-01127-3")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Создаем пользователей
    student = Student("Иван Петров", "S123")
    teacher = Teacher("Анна Иванова", "T456")

    # Показываем доступные книги
    print("\nДоступные книги перед выдачей:")
    library.list_available_books()

    # Пользователи берут книги
    print("\nПроцесс выдачи книг:")
    student.borrow_book(book1)
    student.borrow_book(book2)
    teacher.borrow_book(book3)

    # Пытаемся взять уже взятую книгу
    print("\nПопытка взять недоступную книгу:")
    teacher.borrow_book(book1)

    # Показываем взятые книги у пользователей
    print("\nКниги на руках у пользователей:")
    student.list_borrowed_books()
    teacher.list_borrowed_books()

    # Показываем доступные книги после выдачи
    print("\nДоступные книги после выдачи:")
    library.list_available_books()

    # Поиск книги по названию
    print("\nПоиск книги:")
    found_book = library.find_book_by_title("война и МИР")
    if found_book:
        print(f"Найдена книга: {found_book}")
    else:
        print("Книга не найдена")

    # Возврат книг
    print("\nПроцесс возврата книг:")
    student.return_book(book1)
    teacher.return_book(book3)

    # Показываем доступные книги после возврата
    print("\nДоступные книги после возврата:")
    library.list_available_books()

    # Удаление книги из библиотеки
    print("\nУдаление книги из библиотеки:")
    library.remove_book(book2)


if __name__ == "__main__":
    main()
