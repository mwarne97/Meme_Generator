"""IngestCSV is an Ingestor."""
from .IngestorInterface import IngestorInterface
from .models import QuoteModel
from typing import List
import pandas


class IngestCSV(IngestorInterface):
    """An Ingestor for parsing CSV (Comma-Separated Value) files.

    IngestCSV determines if the file has the extension '.csv' before parsing.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Determine if file (path) is a CSV for parsing.

        Arguments:
            path {str} -- path of file to be parsed.
        """

        try:
            cls.can_ingest(path)
        except Exception:
            raise Exception("Cannot Ingest Exception")

        quotes = []
        data = pandas.read_csv(path, header=0)

        for index, row in data.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
