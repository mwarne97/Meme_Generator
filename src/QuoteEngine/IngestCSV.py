from .IngestorInterface import IngestorInterface
from .models import QuoteModel
from typing import List
import pandas


class IngestCSV(IngestorInterface):
    """"""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """"""
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
