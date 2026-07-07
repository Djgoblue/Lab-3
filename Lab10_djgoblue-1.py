"""
Program Name: Word Count
Author: Daniel Joo
Purpose: Lets the user select a text file and recieve a report 
of the count of every word in the file.
Starter Code: None
Date: July 5, 2026
"""

from pathlib import Path
import string
 
class WordAnalyzer:
    #Initializes the WordAnalyzer class and a dictionary
    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}