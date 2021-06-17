class QuoteModel:
    """"""

    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __str__(self):
        return self.body + " - " + self.author

    def __repr__(self):
        return f"QuoteModel(body={self.body!r}, author={self.author})"
