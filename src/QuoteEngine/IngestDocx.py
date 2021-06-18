"""IngestDocx is an Ingestor"""
from .IngestorInterface import IngestorInterface
from .models import QuoteModel
from typing import List
import docx


class IngestDocx(IngestorInterface):
    """An Ingestor for parsing docx files

    IngestDocx determines if the file has the extension '.docx' before parsing
    """
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Determine if the file (path) is a docx type file for parsing

        Arguments:
            path {str} -- path of file to be parsed
        """
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
