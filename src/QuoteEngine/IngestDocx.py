from .IngestorInterface import IngestorInterface
from .models import QuoteModel
from typing import List
import docx


class IngestDocx(IngestorInterface):
    """"""
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """"""
        try:
            cls.can_ingest(path)
        except Exception:
            raise Exception("Cannot Ingest Exception")

        quotes = []
        data = docx.Document(path)

        for paragraph in data.paragraphs:
            if paragraph.text != "":
                parse = paragraph.text.split("-")
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
