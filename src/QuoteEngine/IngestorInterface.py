"""IngestorInterface is the base for different types of Ingestors."""
from abc import ABC, abstractmethod
from typing import List
from .models import QuoteModel


class IngestorInterface(ABC):
    """An interface for which different types of Ingestors will
    inherit from.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Determines if the the file (path) can be ingested for parsing
        by a particular Ingestor.

        Arguments:
            path {str} -- path for file to be ingested.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract class for parsing data from a given file.

        Arguments:
            path {str} -- path of file to be parsed.
        """
        pass
