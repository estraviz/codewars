# Generating Markdowns
from abc import ABC
from abc import abstractmethod


class Markdown(ABC):

    def __init__(self, text, url_or_language):
        self.text = text
        self.url_or_language = url_or_language

    @abstractmethod
    def generate(self):
        pass


class Link(Markdown):

    def generate(self):
        return f"[{self.text}]({self.url_or_language})"


class Image(Markdown):

    def generate(self):
        return f"![{self.text}]({self.url_or_language})"


class Code(Markdown):

    def generate(self):
        return f"```{self.url_or_language}\n{self.text}\n```"


def generate_markdowns(markdown, text, url_or_language):
    if markdown == "link":
        return Link(text, url_or_language).generate()
    if markdown == "img":
        return Image(text, url_or_language).generate()
    if markdown == "code":
        return Code(text, url_or_language).generate()
