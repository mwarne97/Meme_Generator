class QuoteModel:
    """A quote model.

    A quote model comprises a body of text and an author, both of which are required.
    """

    def __init__(self, body: str, author: str):
        """Create a new 'QuoteModel'.

        Arguments:
            body {str} -- the body of text for the quote.
            author {str} -- the name of the person who said the quote.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return 'str(self)'."""
        return self.body + " - " + self.author

    def __repr__(self):
        """Return 'repr(self)', a computer-readable string representation of this object"""
        return f"QuoteModel(body={self.body!r}, author={self.author})"
