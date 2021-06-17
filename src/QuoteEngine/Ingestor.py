from typing import List
from .IngestorInterface import IngestorInterface
from .models import QuoteModel
from .IngestDocx import IngestDocx
from .IngestCSV import IngestCSV
from .IngestPDF import IngestPDF
from .IngestTxt import IngestTxt


class Ingestor(IngestorInterface):
    """"""

    ingestors = [IngestDocx, IngestCSV, IngestPDF, IngestTxt]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
