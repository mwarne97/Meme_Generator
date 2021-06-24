"""IngestorInterface is the base for different types of Ingestors."""
from abc import ABC, abstractmethod
from typing import List
from .models import QuoteModel


class IngestorInterface(ABC):
    """An interface for which different types of Ingestors will inherit."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Determine if the the file (path) can be ingested for parsing by a particular Ingestor."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract class for parsing data from a given file."""
        pass
