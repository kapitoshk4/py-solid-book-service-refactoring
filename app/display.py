from abc import ABC, abstractmethod

from app.book import Book


class DisplayProcessor(ABC):
    @abstractmethod
    def display(self, book: Book):
        pass


class ConsoleDisplay(DisplayProcessor):
    def display(self, book: Book):
        print(book.content)


class ReverseDisplay(DisplayProcessor):
    def display(self, book: Book):
        print(book.content[::-1])
