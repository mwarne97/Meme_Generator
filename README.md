# Create memes from either locally stored images or from image URLs

This project allows users to generate memes using either images they have locally stored on their computer, or by 
using image URLs. 

## Overview

This project mainly uses the following modules found in the `src` folder:

 - `meme.py`: This randomly generates .png memes from locally stored images by using text from either locally 
   stored docx, pdf, csv, or txt files, or by entering text through the command line. 
   
   Command line options: 
      - `--path`: path of image to be converted to meme
      - `--body`: body of text to be written to meme
      - `--author`: name of meme's author 
   
N.B) `--author` must be given if `--body` was entered manually.
 
 - `app.py`: Implements a web server for generating memes in two ways:
      
   - Randomly by using locally stored images and text from either 
   docx, pdf, csv, or text files
  
   - Through a web-based form for entering an image's URL, the body of text for the meme, and the meme's author.
   
## Sub-Modules

The QuoteEngine directory contains the following sub-modules:

 - `models.py`: Used to represent both the body of the meme's text, and the meme's author
 

 - `IngestCSV.py`: Used to parse text from CSV files for memes by using the `pandas` dependency.
 
 
 - `IngestDocx.py`: Used to parse text from Docx files for memes by using the `python-docx` dependency.

 
 - `IngestPDF.py`: Used to parse text from PDF files for memes by making use of xpdf's `pdftotext` tool.


 - `IngestTxt.py`: Used to parse text from text files for memes.

 
 - `Ingestor.py`: Used to choose the appropriate ingestor for parsing files of a given extension.


 - `IngestorInterface.py`: The abstract base class from which the following ingestors inherit:
      -  `Ingestor.py`
      -  `IngestPDF.py`
      -  `IngestCSV.py`
      -  `IngestDocx.py`
      -  `IngestTxt.py`


The MemeEngine directory contains the `MemeEngine.py` module.

`MemeEngine.py` generates a new meme from a given image, body of text, and author by making use of the `pillow` 
dependency.

## Setting-Up & Running The Programs

N.B) Ensure that python 3 is running on your machine before attempting to execute either program.

Both `app.py` and `meme.py` can be run from the terminal (command prompt).

To run, first change your current working directory to the meme generator's `src` directory. From there, type either  
of the following into the command prompt to run either program respectively:
 - `py app.py` or `python3 app.py`
 - `py meme.py` or `python3 meme.py`
