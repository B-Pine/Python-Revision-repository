# This document will be used to study compositions in python
class Tag:

    def __init__(self, name, content):
        self.opening_tag = f"<{name}>"
        self.closing_tag = f"</{name}>"
        self.contents = content

    def __str__(self):
        return f"{self.opening_tag}{self.contents}{self.closing_tag}"

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__("!DOCTYPE html", "")
        self.closing_tag = ""


class Head(Tag):

    def __init__(self, title=''):
        super().__init__('head', title)
        self._title = title
        title_tag = Tag('title', self._title)
        self.contents = str(title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        self._body_content = []

    def add_tag(self, name, content):
        new_tag = Tag(name, content)
        self._body_content.append(new_tag)

    def display(self, file=None):
        for tag in self._body_content:
            self.contents += str(tag)
        super().display(file=file)


class HtmlDoc:

    def __init__(self, title='document'):
        self._doc_type = DocType()
        self._body = Body()
        self._head = Head(title)

    def add_tag(self, name, content):
        self._body.add_tag(name, content)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</html>", file=file)


if __name__ == "__main__":
    doc = HtmlDoc('This is html document')
    doc.add_tag('h1', 'This is heading 1')
    doc.add_tag('h2', 'This is heading 2')
    doc.add_tag('p', 'This is the paragraph')
    with open('html_document.html', 'w') as html_document:
        doc.display(file=html_document)

