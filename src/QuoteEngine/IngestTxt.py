"""IngestTxt is an Ingestor."""
from .IngestorInterface import IngestorInterface
from .models import QuoteModel
from typing import List
from Exceptions.Exceptions import InvalidFileExtension


class IngestTxt(IngestorInterface):
    """An Ingestor for parsing Text files.

    IngestTxt determines if the file has the extension '.txt' before parsing.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Determine if file (path) is a text file for parsing."""
        try:
            cls.can_ingest(path)
        except InvalidFileExtension:
            raise InvalidFileExtension(f"Cannot Ingest This File: {path}")

        data_file = open(path, 'r')
        quotes = []
        for line in data_file.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed_line = line.split('-')
                new_quote = QuoteModel(parsed_line[0], parsed_line[1])
                quotes.append(new_quote)
        data_file.close()
        return quotes
