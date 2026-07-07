"""
Program Name: Word Analyzer
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

    #Contains main logic
    def process_file(self):
        file = None
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError(f"File not found: {self.__filepath}")
            
            file = self.__filepath.open(encoding="utf-8")
            #Create translation table to remove punctuation
            translator = str.maketrans("", "", string.punctuation)

            for line in file:
                #Split the line into words
                cleaned = line.translate(translator).lower().strip()
                words = cleaned.split()
                #Update the frequency counts
                for word in words:
                    if word in self.__frequencies:
                        self.__frequencies[word] += 1
                    else:
                        self.__frequencies[word] = 1
            return True
        
        except FileNotFoundError:
            print(f"File not found: {self.__filepath}")
            return False
        
        finally:
            if file is not None:
                file.close()

    #Prints the results of the word count
    def print_report(self):
        #Sort the keys alpahetically
        alphabetical = sorted(self.__frequencies.keys())
        for word in alphabetical:
            print(f"{word}: {self.__frequencies[word]}")

#Define main function to run the program
def main():
    library = Path("files")
    #Dictionary of files
    menu = {
    "1": library / "monte_cristo.txt",
    "2": library / "princess_mars.txt",
    "3": library / "Tarzan.txt",
    "4": library / "treasure_island.txt"
    }

    #Display menu
    while True:
        print("\nWord Analyzer")
        print("Select a file to analyze:")
        for key, value in menu.items():
            print(f"{key} {value}")
        print("5. Exit")

        choice = input("Enter your choice (1-5)").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in menu:
            print("Invalid choice. Enter your choice (1-5)")
            continue
            
        selected_file = menu[choice]
        analyzer = WordAnalyzer(selected_file)
        success = analyzer.process_file()
        if success:
            analyzer.print_report()
        else:
            print("Error: could not process file.")
 
if __name__ == "__main__":
    main()