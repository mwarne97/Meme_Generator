"""Exceptions."""


class FileNotFound(Exception):
    """Exception for if the file was not found."""

    pass


class InvalidFilePath(Exception):
    """Exception for if an invalid file path was entered."""

    pass


class InvalidFileExtension(Exception):
    """Exception for if an invalid file extension was given."""

    pass
