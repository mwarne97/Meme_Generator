"""IngestPDF is an Ingestor."""
from .IngestorInterface import IngestorInterface
from .models import QuoteModel
from typing import List
import random
import subprocess
import os


class IngestPDF(IngestorInterface):
    """An Ingestor for parsing PDF files.

    IngestPDF determines if the file has the extension '.pdf' before parsing.
    """
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Determine if file (path) is a PDF for parsing.

        Arguments:
            path {str} -- path of file to be parsed.
        """

        try:
            cls.can_ingest(path)
        except Exception:
            raise Exception("Cannot Ingest Exception")

        tmp_file = f'./{random.randint(0,10000)}.txt'
        program = "./xpdf-tools-win-4.03/bin64/pdftotext.exe"
        subprocess.call([program, path, tmp_file])

        data_file = open(tmp_file, 'r')
        quotes = []
        for line in data_file.readlines():
            line = line.strip('/n/r').strip()
            if len(line) > 0:
                parsed_line = line.split('-')
                new_quote = QuoteModel(parsed_line[0], parsed_line[1])
                quotes.append(new_quote)
        data_file.close()
        os.remove(tmp_file)

        return quotes
