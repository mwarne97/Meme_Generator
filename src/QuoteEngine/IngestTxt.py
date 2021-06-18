"""IngestTxt is an Ingestor."""
from .IngestorInterface import IngestorInterface
from .models import QuoteModel
from typing import List


class IngestTxt(IngestorInterface):
    """An Ingestor for parsing Text files.

    IngestTxt determines if the file has the extension '.txt' before parsing.
    """
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Determine if file (path) is a text file for parsing.

        Arguments:
            path {str} -- path of file to be parsed.
        """
        try:
            cls.can_ingest(path)
        except Exception:
            raise Exception("Cannot Ingest Exception")

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
