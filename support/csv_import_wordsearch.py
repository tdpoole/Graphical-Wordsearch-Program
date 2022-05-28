import csv
from wordsearchclass import Wordsearch
from support import settings
import pickle

# Function to import, solve, then initialise and serialise the corresponding wordsearch object.
def import_wordsearch_from_file(file):
    try:
        with open(file, "r", newline="") as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        return False, 1

    for row in data:
        for letter in row:
            if not letter in settings.ALPHABET:
                return False, 2
    return Wordsearch(data)


if __name__ == "__main__":
    import main
