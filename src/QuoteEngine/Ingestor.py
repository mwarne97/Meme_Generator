"""Ingestor stores different types of Ingestors for parsing files."""
from typing import List
from .IngestorInterface import IngestorInterface
from .models import QuoteModel
from .IngestDocx import IngestDocx
from .IngestCSV import IngestCSV
from .IngestPDF import IngestPDF
from .IngestTxt import IngestTxt


class Ingestor(IngestorInterface):
    """Comprises a list of different ingestors for reading different file formats."""

    ingestors = [IngestDocx, IngestCSV, IngestPDF, IngestTxt]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Determine which ingestor can parse the given file (path)."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
