import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

from app.book import Book


class SerializeProcessor(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> None:
        pass


class JSONSerializer(SerializeProcessor):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XMLSerializer(SerializeProcessor):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
