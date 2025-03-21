# imageSort
Python script to sort data from a CSV file. Used to iterate through CSV/Spread sheet, create a folder for each primary ID, and add all data from csv relating to primary ID into its respective folder. Includes supplemental script to sort the new folders, based on the number of files in each folder.

For 8plus.py:

python 8plus.py *path to directory* *threshold number of files*

for example, if I want to create a new directory for each folder with 10 files, we would use
python 8plus.py C:\Users\Path 10
