from BookStoreApi.Book_Models.baseObj import BaseObj


class BookModel(BaseObj):
    def __init__(self, isbn: str, title: str, subTitle: str = None, author: str = None,
                 publish_date: str = None, publisher: str = None, pages: int = 0, description: str = None,
                 website: str = None):
        super(BaseObj, self).__init__()
        self._website = website
        if not isinstance(isbn, str):
            raise TypeError("isbn not string")
        self._isbn = isbn
        if not isinstance(title, str):
            raise TypeError("title not string")
        self._title = title
        if not isinstance(subTitle, str) and subTitle is not None:
            raise TypeError("subTitle not string")
        self._subTitle = subTitle
        if not isinstance(author, str) and author is not None:
            raise TypeError("author not string")
        self._author = author
        if not isinstance(publish_date, str) and publish_date is not None:
            raise TypeError("publish_date not string")
        self._publish_date = publish_date
        if not isinstance(publisher, str) and publisher is not None:
            raise TypeError("publisher not string")
        self._publisher = publisher
        if not isinstance(pages, int) and pages is not 0:
            raise TypeError("pages not int")
        self._pages = pages
        if not isinstance(description, str) and description is not None:
            raise TypeError("description not string")
        self._description = description
        if not isinstance(website, str) and website is not None:
            raise TypeError("website not string")

    @property
    def isbn(self):
        """Gets the isbn of this Order.
        :return: The isbn of this Order.
        :rtype: str
        """
        return self._isbn
